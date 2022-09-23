#!/usr/bin/python3
"""Send request to url, display X-Request-Id"""


import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    body = requests.get(url)
    print(body.headers.get('X-Request-Id'))
