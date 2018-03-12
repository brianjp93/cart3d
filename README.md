# Hello
Only parts of the Product and Order API wrapper are written so far cuz I'm a lazy boi and I don't need them yet.

## Usage

- Initialize the client.
- Either access_token or token can be given.
```python
>>> import cart3d
>>> client = cart3d.Client(<client_id>, <client_secret>, token=<token>, access_token=<access_token>, secureURL=<secureURL>)
```

### Products

- Get all products
```python
>>> r = client.products.get()
>>> r.json()
    {... json data ...}
```

- Get specific product by SKU
```python
>>> r = client.products.get(sku='ab1234')
>>> r.json()
    {... json data ...}
```