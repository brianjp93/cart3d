"""
cart3d.py

The base wrapper file for the 3dcart REST API. Uses files
    from the resources folder to connect different endpoints
    in the 3dcart api.

Documentation
-------------
https://apirest.3dcart.com/swagger/ui/index#/

Examples
--------
# initalize
>>> import cart3d
>>> client = cart3d.Client(<client_id>, <client_secret>, access_token=<str>, secure_url=<str>)

# get products
>>> r = client.products.get()
>>> r.json()

# get specific SKU
>>> r = client.products.get(sku='1234')
>>> r.json()

# get orders
>>> r = client.orders.get()
>>> r.json()

"""
from __future__ import print_function, division
import logging
import requests
import resources

logger = logging.getLogger(__name__)

__author__ = 'Brian Perrett'
__date__ = '2018-01-31'


class Client():
    """Base class for connecting to 3DCart.

    Contains the methods for authorizing a client account.
    Initializes [Products, Orders, ...] classes as attributes of this object.

    """

    base = 'https://apirest.3dcart.com/'

    def __init__(self, client_id, client_secret, token=None, access_token=None, secure_url=None):
        """Initialize the Cart3d object.

        Only needs one of token/access_token

        Parameters
        ----------
        client_id : str
        client_secret : str
        token : str
        access_token : str
        secure_url : str
            The https url for the store being accessed.

        Returns
        -------
        None

        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token
        self.access_token = access_token
        self.secure_url = secure_url

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
            'SecureURL': self.secure_url,
            'PrivateKey': self.client_secret
        }
        if self.token is not None:
            headers['Token'] = self.token
        elif self.access_token is not None:
            headers['Authorization'] = 'Bearer {}'.format(self.access_token)
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
        else:
            params['store_url'] = self.secure_url
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
        else:
            params['store_url'] = self.secure_url
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