num = int(input('Enter a number : '))
num1, num2 = num, num
sum = 0
while num:
    sum += 1
    num //= 10
temp = 0
while num2:
    temp = temp + pow(num2 % 10, sum)
    num2 //= 10
if num1 != temp:
    print('Entered number is not Armstrong')
else:
    print('Entered number is an Armstrong')
