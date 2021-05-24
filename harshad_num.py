def harshad_num(num):
    result = 0
    temp = num
    while num:
        res = num % 10
        num = num // 10
        result += res
    if temp % result == 0:
        return True
    return False


input = int(input('Enter a number : '))
print(harshad_num(input))
