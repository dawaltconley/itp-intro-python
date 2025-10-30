# Using fakestoreapi.com
import requests

domain = 'https://fakestoreapi.com'

def truncate(string: str, n: int) -> str:
    if len(string) > n:
        return string[:n][:-3] + '...'
    return string

def get_products():
    return requests.get(domain + '/products').json()

def get_product_price(product):
    return product['price']

def get_product_rating(product):
    return product['rating']['rate']

def get_most_expensive_product():
    return max(get_products(), key=get_product_price)

def get_least_expensive_product():
    return max(get_products(), key=lambda p: p['price'])

def get_best_rated_product():
    return max(get_products(), key=get_product_rating)

def get_worst_rated_product():
    return min(get_products(), key=get_product_rating)

def list_by_rating():
    products = sorted(get_products(), key=get_product_rating, reverse=True)
    for p in products:
        print(str(get_product_rating(p)).ljust(6) + p['title'])

def list_by_price():
    products = sorted(get_products(), key=get_product_price)
    for p in products:
        title = p['title']
        price = str(get_product_price(p))
        string = price.ljust(8) + title
        print(truncate(string, 40))

list_by_price()
