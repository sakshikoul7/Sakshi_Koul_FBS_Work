#WAP to print Armstrong number within a given range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Armstrong numbers in the range are:")
for num in range(lower, upper + 1):
    order = len(str(num))
    sum_of_digits = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** order
        temp //= 10
    if num == sum_of_digits:
        print(num)