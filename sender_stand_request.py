import requests
import configuration
import data


def post_products_kits():
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=data.product_ids,
                         headers=data.headers)


response = post_products_kits()
print(response.status_code)
print(response.json())
