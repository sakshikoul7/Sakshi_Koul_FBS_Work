for i in range(1,6):
    for j in range(1, 6-i):
        print(" ", end="")
    num=1
    for j in range(6-i, 5+i):
        print(chr(64+num), end= '')
        num += 1
    print()