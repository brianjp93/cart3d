"""
"""
import logging
import requests

logger = logging.getLogger(__name__)

class Orders():

    def __init__(self, parent):
        self.parent = parent

    def get(self, **kwargs):
        """Get list of orders.

        Parameters
        ----------
        invoicenumber : int
        orderstatus : str
            []
        datestart : str
            mm/dd/yyyy
        dateend : str
            mm/dd/yyyy
        limit : int
            default : 300
        offset : int
            default : 1
        countonly : int
            [-1, 1]
        lastupdatestart : str
            mm/dd/yyyy
        lastupdateend : str
            mm/dd/yyyy

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Orders'.format(self.parent.base)
        headers = self.parent.get_headers()
        params = {
            'limit': 300,
            'offset': 1
        }
        for kwarg, val in kwargs.items():
            params[kwarg] = val
        r = requests.get(url, headers=headers, params=params)
        return r

    def update(self, orders):
        """Update a collection of orders.

        Parameters
        ----------
        orders : list

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Orders'.format(self.parent.base)
        headers = self.parent.get_headers()
        data = {'orders': orders}
        r = requests.put(url, data=data, headers=headers)
        return r

    def get_id(self, order_id):
        """Get an order by ID.

        Parameters
        ----------
        order_id : int

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Orders/{}'.format(self.parent.base, order_id)
        headers = self.parent.get_headers()
        r = requests.get(url, headers=headers)
        return r

    def get_shipments(self, order_id):
        """Get shipments for an order.

        Parameters
        ----------
        order_id : int

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Orders/{}/Shipments'.format(self.parent.base, order_id)
        headers = self.parent.get_headers()
        r = requests.get(url, headers=headers)
        return r

    def update_shipments(self, order_id, shipments):
        """Update shipments for an order.

        Parameters
        ----------
        order_id : int
        shipments : dict

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Orders/{}/Shipments'.format(self.parent.base, order_id)
        headers = self.parent.get_headers()
        params = {'shipments': shipments}
        r = requests.put(url, headers=headers, params=params)
        return r

    def get_items(self, order_id):
        """Get items for an order.

        Parameters
        ----------
        order_id : int

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Orders/{}/Items'.format(self.parent.base, order_id)
        headers = self.parent.get_headers()
        r = requests.get(url, headers=headers)
        return r

    def get_transactions(self, order_id):
        """Get transactions for an order.

        Parameters
        ----------
        order_id : int

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Orders/{}/Transactions'.format(self.parent.base, order_id)
        headers = self.parent.get_headers()
        r = requests.get(url, headers=headers)
        return r