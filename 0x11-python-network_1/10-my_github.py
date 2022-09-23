#!/usr/bin/python3
"""9. My GitHub! Python script that takes your GitHub credentials"""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    ath = HTTPBasicAuth(username, password)
    body = requests.get("https://api.github.com/user", ath)
    print(body.json().get("id"))
