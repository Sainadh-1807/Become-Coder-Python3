row_count = int(input("Enter number of rows : "))

for i in range(1, row_count + 1):
    for j in range(1, i + 1):
        print(i, end=" ")

    print("\n")