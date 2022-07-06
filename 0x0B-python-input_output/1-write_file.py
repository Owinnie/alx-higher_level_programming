#!/usr/bin/python3

"""Write a function that writes a string
to a text file (UTF8) and returns the
number of characters written"""


import json


def write_file(filename="", text=""):
    """"Writing"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
