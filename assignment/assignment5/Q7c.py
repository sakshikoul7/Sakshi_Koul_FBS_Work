#Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter the number:"))
sum = 0
for i in range(0, n + 1):
    sum = sum + (2**i)
print("The sum of the series is:", sum)
