#!/usr/bin/python3
"""Takes URL, and email, sends POST request with email """


from sys import argv
from urllib import request
from urllib import parse

if __name__ == "__main__":
    url = argv[1]
    email = {"email": argv[2]}
    data = parse.urlencode(email)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
