#Write a program to calculate the sum of following series where n is input by user. 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!
n = int(input("Enter the number:"))
factorial = 1
sum = 0
for i in range(1, n+1):
    factorial= factorial*i
    sum=(i/factorial) +sum 
print("THe sum of the series is:",sum)
