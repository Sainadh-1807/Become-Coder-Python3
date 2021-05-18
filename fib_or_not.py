import math

# if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

# if n is a Fibinacci Number
def isFibonacci(n):
    # if one of 5*n*n + 4 or 5*n*n - 4 or both is a perferct square
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

for i in range(1, 31):
    if (isFibonacci(i) == True):
        print(i, "is a Fibonacci Number")
    else:
        print(i, "is a not Fibonacci Number")
