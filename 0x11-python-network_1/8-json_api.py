#!/usr/bin/python3
"""JSON: module that takes a letter and sends POST"""


import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""
    values = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"
    body = requests.post(url, values)
    try:
        body.raise_for_status()
        json = body.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print("Not a valid JSON")
