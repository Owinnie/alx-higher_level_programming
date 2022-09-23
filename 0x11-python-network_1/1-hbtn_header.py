#!/usr/bin/python3
"""takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id
found in the header of the response"""


from sys import argv
from urllib import request

with request.urlopen(argv[1]) as response:
    att_header = response.info()["X-Request-Id"]
    print(att_header)
