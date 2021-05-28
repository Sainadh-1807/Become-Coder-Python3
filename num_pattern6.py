row_count = int(input("Enter count of rows: "))

for i in range(1, row_count + 1):
    for j in range(1, row_count + 1):
        if j % 2 == 0:
            print('0', end=" ")
        else:
            print('1', end=" ")
    print("\n")
