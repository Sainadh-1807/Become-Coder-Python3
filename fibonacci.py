def gen_fib(num, a = 0, b = 1):
    if num == 0:
        return
    if num == 1:
        print(0)
        return
    a, b = 0, 1
    print(a, b, end=' ')
    for i in range(3, num + 1):
        c = a + b
        print(c, end=' ')
        a = b
        b = c


num = int(input())
gen_fib(num)
