#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nw_ls = []
    ans = 0
    for i in range(0, list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except TypeError:
            ans = 0
            print("wrong type")
        except ZeroDivisionError as err2:
            ans = 0
            print(err2)
        except IndexError:
            ans = 0
            print("out of range")
        finally:
            pass
        nw_ls.append(ans)
    return nw_ls
