"""
orders.py
"""
import logging
import requests

logger = logging.getLogger(__name__)

class Orders():

    def __init__(self, parent):
        """Initialize Orders object.

        Parameters
        ----------
        parent : obj
            The Cart3d object

        Returns
        -------
        None

        """
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

        Notes
        -----
        Date starts and ends are inclusive.

        Examples
        --------
        >>> r = client.orders.get()
        >>> r.json()
            [{order_data}, {order_data}, ...]

        """
        allowed_params = {
            'datestart', 'dateend', 'invoicenumber', 'orderstatus',
            'limit', 'offset', 'countonly', 'lastupdatestart', 'lastupdateend',
        }
        url = '{}3dCartWebAPI/v1/Orders'.format(self.parent.base)
        headers = self.parent.get_headers()
        params = {
            'limit': 100,
            'offset': 1
        }
        for kwarg, val in kwargs.items():
            if kwarg in allowed_params:
                # only add kwarg to params if its value is not None
                if val is not None:
                    params[kwarg] = val
            else:
                raise ValueError('{} is not a valid parameter of this function.'.format(kwarg))
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
        r = requests.put(url, json=orders, headers=headers)
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
        r = requests.put(url, headers=headers, json=shipments)
        return r

    def create_shipments(self, order_id, **kwargs):
        """Add a shipment to an order.

        https://apirest.3dcart.com/swagger/ui/index#!/Orders/Orders_Post_0_1_2

        Parameters
        ----------
        order_id : int
        ShipmentFirstName : str
        ShipmentLastName : str
        ShipmentID : int
            optional?
        ShipmentBoxes : int
            optional?
        ShipmentInternalComment : str
        ShipmentOrderStatus : int
            optional?
        ShipmentAddress : str
            first line of address
        ShipmentAddress2 : str
            second line of address
        ShipmentAlias : str
            what now
        ShipmentCity : str
        ShipmentCompany : str
        ShipmentCost : float
        ShipmentCountry : str
        ShipmentEmail : str
        ShipmentMethodID : int
        ShipmentMethodName : str
        ShipmentShippedDate : str
            unknown format
        ShipmentPhone : str
        ShipmentState : str
        ShipmentZipCode : str
        ShipmentTax : float
        ShipmentWeight : float
            What units..?
        ShipmentTrackingCode : str
        ShipmentUserID : int
            what.  Why is the documentation for the 3dcart api so god awful.
        ShipmentNumber : int
            ???
            The only thing 3dcart tells me for this is...
            database reference = orders_shipments.shipment_number
            wtf does that mean.
        ShipmentAddressTypeID : int
            What is this.

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Orders/{}/Shipments'.format(self.parent.base, order_id)
        headers = self.parent.get_headers()
        shipment = {}
        for kwarg, val in kwargs.items():
            shipment[kwarg] = val
        r = requests.post(url, headers=headers, json=shipment)
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
