#!/usr/bin/bash
def print_last_digit(number):
    ld = int(repr(number)[-1])
    print("{}".format(ld), end="")
    return ld
