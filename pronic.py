import math


def pronic_check(n):
    x = int(math.sqrt(n))
    if x * (x + 1) == n:
        return True
    else:
        return False


num = int(input('Enter a number : '))

if pronic_check(num) == True:
    print(num, "is a pronic number")
else:
    print(num, "is not a pronic number")
