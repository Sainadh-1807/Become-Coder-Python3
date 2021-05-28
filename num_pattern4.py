row_count = int(input("Enter count of rows: "))

for i in range(1, row_count+1):
    for j in range(1, row_count+1):
        if j == 1 :
            print(i, end=" ")
        else:
            print(j, end = " ")
    print("\n")
    