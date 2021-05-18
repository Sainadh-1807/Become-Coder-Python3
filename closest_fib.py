from math import *

n = int(input("Enter a number:"))

if sqrt(5 * n ** 2 + 4) % 1 == 0 or sqrt(5 * n ** 2 - 4) % 1 == 0:
    print(n, "is a Fibonacci number")
else:
    print(n, "is not a Fibonacci number")
    c = 0
    while 1:
        c += 1
        if sqrt(5 * (n + c) ** 2 + 4) % 1 == 0 or sqrt(5 * (n + c) ** 2 - 4) % 1 == 0:
            print("%s is the closest Fibonacci number" % str(n + c))
            break
        if sqrt(5 * (n - c) ** 2 + 4) % 1 == 0 or sqrt(5 * (n - c) ** 2 - 4) % 1 == 0:
            print("%s is the closest Fibonacci number" % str(n - c))
            break
