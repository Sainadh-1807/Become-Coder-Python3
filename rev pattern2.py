row_count = int(input("Enter number of rows : "))

for i in range(row_count,0, -1):
    for j in range(i):
        print(i, end=" ")

    print("\n")