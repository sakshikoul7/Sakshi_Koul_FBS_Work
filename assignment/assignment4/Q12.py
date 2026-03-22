# Program to check if a number is an Armstrong Number

num = int(input("Enter a number: "))
temp = num
digits = len(str(num))   # count digits
sum_of_powers = 0

while temp > 0:
    digit = temp % 10   # extract last digit
    sum_of_powers += digit ** digits   # raise digit to power of total digits
    temp //= 10         # remove last digit

if sum_of_powers == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
