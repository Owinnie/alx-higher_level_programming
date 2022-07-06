#!/usr/bin/python3
"""reading file"""


def read_file(filename=""):
    """reading file"""
    with open(filename, encoding="UTF8") as f:
        print(f.read())
