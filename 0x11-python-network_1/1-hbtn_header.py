#!/usr/bin/python3
"""Takes URL, sends request, displays value X-Request-Id."""


from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        att_header = response.info()["X-Request-Id"]
        print(att_header)
