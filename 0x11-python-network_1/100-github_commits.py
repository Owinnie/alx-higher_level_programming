#!/usr/bin/python3
"""10. Time for an interview!"""


from sys import argv
import requests

if __name__ == "__main__":
    # Arguments--> arg1: repo name, arg2: repo owner
    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print(f"{commits[i]['sha']}:
                    {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
