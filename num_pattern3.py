row_count = int(input("Enter count of rows: "))

for i in range(1, row_count+1):
    if i % 2 == 0:
        for j in range(1, row_count+1):
            print(j, end=" ")
    else:
        for j in range(1, row_count+1):
            print(i, end = " ")
    print("\n")
