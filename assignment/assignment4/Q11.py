#to check if given number Strong Number.
num = int(input("Enter a number: "))
temp = num
sum_of_factorials = 0

while temp > 0:
    digit = temp % 10   # extract last digit
    fact = 1
    i = 1
    while i <= digit:   # calculate factorial of digit
        fact *= i
        i += 1
    sum_of_factorials += fact
    temp //= 10   # remove last digit

if sum_of_factorials == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")

