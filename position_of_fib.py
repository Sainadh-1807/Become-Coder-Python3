def fib(number, start=0, a=0, b=1, c=0):
    while c < number:
        c = a + b   # sum of a n b assigned to c
        a = b       # b assigned to a
        b = c       # c assigned to c
        start += 1  # start i.e., position is incremented by 1 (0 --> 1)
    if number == 0:
        print(1)
        return
    elif number == 1:
        print(2)
        return
    elif number != c:
        print(False, 'coz', number, 'is not a fibonacci number')
    else:
        print(number, 'is located in', start + 2, 'th', 'position')


num = int(input('Enter a number : '))
fib(num)
