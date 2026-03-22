# Program to print numbers in a range divisible by a given number

n = int(input("Enter the value of n (upper limit): "))
divisor = int(input("Enter the divisor: "))

print(f"Numbers up to {n} divisible by {divisor}:")

i = 1
while i <= n:
    if i % divisor == 0:   # check divisibility
        print(i, end=" ")
    i += 1
