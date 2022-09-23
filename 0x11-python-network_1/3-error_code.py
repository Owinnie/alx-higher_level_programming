#!/usr/bin/python3
"""Takes URL, and email, sends request, Handles HTTPError."""


from sys import argv
from urllib import request
from urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
