#!/usr/bin/python3
"""Send request to url, with variable email"""


import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    body = requests.post(url, data=values)
    print(body.text)
