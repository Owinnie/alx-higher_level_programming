#!/usr/bin/python3
def uppercase(str):
    s = ""
    for c in str:
        if ord(c) == 32:
            s += c
        elif 65 < ord(c) < 90:
            s += c
        else:
            s += chr(ord(c) - 32)
    print(s)
