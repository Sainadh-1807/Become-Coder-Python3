row_count = int(input("Enter count of rows: "))
temp = 0
for i in range(1, row_count):
    for j in range(1, row_count + 1):
        if temp == 0:
            temp = 1
            print(temp, end=" ")
        else:
            temp = 0
            print(temp, end=" ")
    print("\n")
