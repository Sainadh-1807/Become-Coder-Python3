def fibb(a, b, d, num):
    if d > num:
        return
    elif d == 1:
        print(a, end=' ')
        d += 1
    elif d == 2:
        print(b, end=' ')
        d += 1
    print(a + b, end=' ')
    fibb(b, a + b, d + 1, num)


num = int(input('Enter : '))
fibb(0, 1, 1, num)
