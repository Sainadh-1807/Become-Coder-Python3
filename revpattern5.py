row_count = int(input("Enter number of rows : "))

for i in range(row_count, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")

    print("\n")
