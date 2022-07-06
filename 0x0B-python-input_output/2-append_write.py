#!/usr/bin/python3

"""Write a function that appends
a string at the end of a text
file (UTF8)"""


import json


def append_write(filename="", text=""):
    """Append"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)