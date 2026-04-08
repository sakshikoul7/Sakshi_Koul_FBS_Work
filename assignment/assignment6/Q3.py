n = 4

for i in range(n):
    # spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # numbers
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()