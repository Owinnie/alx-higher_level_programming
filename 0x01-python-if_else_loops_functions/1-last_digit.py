#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", end=" ")
print("{} is {}".format(number, int(str(number)[-1])), end=" ")
if int(str(number)[-1]) == 0:
    print("and is 0")
elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0:
    print("and is less than 6 and not 0")
elif int(str(number)[-1]) > 5:
    print("and is greater than 5")