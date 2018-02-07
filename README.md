# Hello
Only parts of the product and order api wrapper are written so far

## Usage
```python
>>> from cart3d import Cart3d
>>> api = Cart3d(<client_id>, <client_secret>, token=<token>, secureURL=<secureURL>)
>>> # get products
>>> r = api.products.get()
>>> r.json()
    {... data ...}
```