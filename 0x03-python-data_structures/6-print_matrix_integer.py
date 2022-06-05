#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ls in matrix:
        for ele_i in range(len(ls)):
            print("{:d}".format(ls[ele_i]), 
                end="" if ele_i == len(ls) - 1 else " ")
        print("")
