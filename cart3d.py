"""
"""
from __future__ import absolute_import, print_function, division
import logging
import requests
import resources

logger = logging.getLogger(__name__)

__author__ = 'Brian Perrett'
__date__ = '2018-01-31'


class Cart3d():

    base = 'https://apirest.3dcart.com/'

    def __init__(self, client_id, client_secret, token=None, secureURL=None):
        """Initialize the Cart3d object.

        Parameters
        ----------
        client_id : str
        client_secret : str
        token : str
        secureURL : str
            The https url for the store being accessed.

        Returns
        -------
        None

        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token
        self.secureURL = secureURL

        self.products = resources.Products(self)
        self.orders = resources.Orders(self)

    def get_headers(self):
        """Retreive the api request headers.

        Parameters
        ----------
        None

        Returns
        -------
        dict
            Request headers.  Required for requests to 3dcart api.

        """
        headers = {
            'Accept': 'application/json',
            'SecureURL': self.secureURL,
            'Token': self.token,
            'PrivateKey': self.client_secret
        }
        return headers

    def get_auth_code(self, redirect_uri, state, store_url=None):
        """Get auth code.  First step in oauth procedure.

        Parameters
        ----------
        redirect_uri : str
            URI of where to redirect the user after authorizing connection
        state : str
            Validation string.  Ensure this is returned to you in the redirect
            URI as a parameter.
        store_uri : str
            The URL of the store you are trying to authorize connection to.

        Returns
        -------
        Response

        """
        url = 'https://apirest.3dcart.com/oauth/authorize'
        params = {
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'state': state,
            'response_type': 'code',
        }
        if store_url is not None:
            params['store_url'] = store_url
        r = requests.get(url, params=params)
        return r

    def get_auth_code_url(self, redirect_uri, state, store_url=None):
        """Get the full url for getting the auth code.

        Parameters
        ----------
        redirect_uri : str
            URI of where to redirect the user after authorizing connection
        state : str
            Validation string.  Ensure this is returned to you in the redirect
            URI as a parameter.
        store_uri : The URL of the store you are trying to authorize connection to.

        Returns
        -------
        str
            The full auth code URL with parameters

        """
        url = 'https://apirest.3dcart.com/oauth/authorize'
        params = {
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'state': state,
            'response_type': 'code',
        }
        if store_url is not None:
            params['store_url'] = store_url
        req = requests.Request('POST', url, params=params)
        prepped = req.prepare()
        return prepped.url

    def get_token(self, code):
        """Get token from 3dCart

        Parameters
        ----------
        code : str
            value returned in response from get_auth_code()

        Returns
        -------
        Response

        """
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        url = 'https://apirest.3dcart.com/oauth/token'
        data = {
            'Code': code,
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        r = requests.post(url, data=data, headers=headers)
        return r