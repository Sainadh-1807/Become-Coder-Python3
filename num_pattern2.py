row_count = int(input("Enter count of rows: "))

for i in range(row_count):
    for j in range(row_count):
        if i % 2 == 0:
            print(row_count - j, end=" ")
            continue
        print(j + 1, end=" ")
    print("\n")
