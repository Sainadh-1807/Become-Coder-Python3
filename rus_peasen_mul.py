num1, num2 = map(int, input("Enter a & b : ").split())
ans = 0

while num2 != 0:
    if num2 % 2 != 0:
        ans = ans + num1
        num1 = num1 * 2
        num2 = num2 // 2
    if num2 % 2 == 0:
        num1 = num1 * 2
        num2 = num2 // 2

print("result : ", ans)
