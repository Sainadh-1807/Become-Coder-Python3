# prints fibonacci value within the range of Lower, Upper

def fibonacci(Lower, Upper, a = 0, b = 1):
    if Lower == 0:
        print(a, b, end = ' ')
    if Lower == 1:
        print(b, end = ' ')
    c = 0
    while c <= Upper:
        c = a+b
        if c >= Lower and c <= Upper:
            print(c, end = ' ')
        a = b # 1
        b = c # 2
Lower, Upper = map(int,input().split())
fibonacci(Lower, Upper) # fun calls fibonacci
