#!/usr/bin/python3
"""reading file"""


def read_file(filename=""):
    """reading file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
