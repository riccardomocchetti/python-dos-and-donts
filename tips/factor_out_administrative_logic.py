from functools import cache
import requests


# Don't do this
def fetch_data(url, saved={}):
    if url in saved:
        return saved[url]
    data = requests.get(url).json()
    saved[url] = data
    return data


# Do this instead
@cache
def fetch_data(url):
    return requests.get(url).json()


# Advanced tip - Custom decorator function
from functools import wraps

def my_cache(func):
    saved = {}

    @wraps(func)
    def wrapper(*args):
        if args in saved:
            print("fetching from cache")
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    
    return wrapper


@my_cache
def foo(a, b):
    return a + b


print(foo(2, 3))
print(foo(2, 3))