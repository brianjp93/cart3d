"""
products.py
"""
import logging
import requests

logger = logging.getLogger(__name__)

class Products():

    def __init__(self, parent):
        self.parent = parent

    def get(self, **kwargs):
        """Get all products.

        https://apirest.3dcart.com/swagger/ui/index#!/Products/Products_GetAllProducts

        Parameters
        ----------
        limit : int
        offset : int
        countonly : int
        sku : str
        name : str
        costfrom : float
        costto : float
        pricefrom : float
        priceto : float
        stockfrom : int
        stockto : int
        hide : int
        freeshipping : int
        onsale : int
        nontax : int
        notforsale : int
        giftcertificate : int
        homespecial : int
        categoryspecial : int
        nonsearchable : int
        selfship : int
        rewarddisable : int
        lastupdatestart : str
            mm/dd/yyyy
        lastupdateend : str
            mm/dd/yyyy

        Returns
        -------
        Response
            Product List

        """
        url = '{}3dCartWebAPI/v1/Products'.format(self.parent.base)
        headers = self.parent.get_headers()
        params = {
            'limit': 200,
            'offset': 1,
        }
        for kwarg in kwargs:
            params[kwarg] = kwargs[kwarg]
        r = requests.get(url, headers=headers, params=params)
        return r

    def create(self, **kwargs):
        """
        """
        # TODO
        pass

    def update(self, body):
        """Update a product or list of products.

        https://apirest.3dcart.com/swagger/ui/index#!/Products/Products_Update

        Parameters
        ----------
        body : list
            The update list of skus that need to be updated

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Products'.format(self.parent.base)
        headers = self.parent.get_headers()
        data = {'products': body}
        r = requests.put(url, data=body, headers=headers)
        return r

    def delete(self, catalog_id):
        """Delete a product from 3dcart.

        Parameters
        ----------
        catalog_id : int

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Products/{}'.format(self.parent.base, catalog_id)
        headers = self.parent.get_headers()
        r = requests.delete(url, headers=headers)
        return r

    def get_skuinfo(self, **kwargs):
        """

        Parameters
        ----------
        limit : int, optional
            default: 200
        offset : int, optional
            default : 1
        countonly : int
            [-1, 1]
        sku : str
        name : str

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Products/skuinfo'.format(self.parent.base)
        headers = self.parent.get_headers()
        params = {
            'limit': 200,
            'offset': 1,
        }
        for kwarg in kwargs:
            params[kwarg] = kwargs[kwarg]
        r = requests.get(url, headers=headers, params=params)
        return r

    def get_advanced_options(self, catalog_id):
        """Get the advanced options for a product.

        Parameters
        ----------
        catalog_id : int

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Products/{}/AdvancedOptions'.format(self.parent.base, catalog_id)
        headers = self.parent.get_headers()
        r = requests.get(url, headers=headers)
        return r

    def update_advanced_options(self, catalog_id, advanced_options):
        """Update the collection of advanced options for a product.

        Parameters
        ----------
        catalog_id : int
        advanced_options : list

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Products/{}/AdvancedOptions'.format(self.parent.base, catalog_id)
        headers = self.parent.get_headers()
        data = {'advanced_options': advanced_options}
        r = requests.put(url, headers=headers, data=data)
        return r

    def get_images(self, catalog_id):
        """Get images for a product.

        Parameters
        ----------
        catalog_id : int

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Products/{}/Images'.format(self.parent.base, catalog_id)
        headers = self.parent.get_headers()
        r = requests.get(url, headers=headers)
        return r

    def get_category(self, category_id, **kwargs):
        """Get all products from a specific category

        Paramters
        ---------
        category_id : int
        ...

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Categories/{}/Products'.format(self.parent.base, category_id)
        headers = self.parent.get_headers()
        params = {
            'limit': 200,
            'offset': 1,
        }
        for kwarg in kwargs:
            params[kwarg] = kwargs[kwarg]
        r = requests.get(url, headers=headers, params=params)
        return r

    def get_distributor(self, distributor_id, **kwargs):
        """Get all products from distributor.

        Parameters
        ----------
        distributor_id : int
        ...

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Distributors/{}/Products'.format(self.parent.base, distributor_id)
        headers = self.parent.get_headers()
        params = {
            'limit': 200,
            'offset': 1,
        }
        for kwarg in kwargs:
            params[kwarg] = kwargs[kwarg]
        r = requests.get(url, headers=headers, params=params)
        return r

    def get_manufacturer(self, manufacturer_id, **kwargs):
        """Get all products from a manufacturer.

        Parameters
        ----------
        manufacturer_id : int
        ...

        Returns
        -------
        Response

        """
        url = '{}3dCartWebAPI/v1/Manufacturers/{}/Products'.format(self.parent.base, manufacturer_id)
        headers = self.parent.get_headers()
        params = {
            'limit': 200,
            'offset': 1,
        }
        for kwarg in kwargs:
            params[kwarg] = kwargs[kwarg]
        r = requests.get(url, headers=headers, params=params)
        return r