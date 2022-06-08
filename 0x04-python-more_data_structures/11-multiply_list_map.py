#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    m_dup = my_list[:]
    return list(map(lambda x: x * number, m_dup))

