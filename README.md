# Hello
Only parts of the product and order api wrapper are written so far

## Usage

- Initialize the client.
```python
>>> from cart3d import Cart3d
>>> client = Cart3d(<client_id>, <client_secret>, token=<token>, secureURL=<secureURL>)
```

### Products

- Get all products
```python
>>> r = client.products.get()
>>> r.json()
    {... data ...}
```

- Get specific product by SKU
```python
>>> r = client.products.get(sku='ab1234')
>>> r.json()
    {... json data ...}
```