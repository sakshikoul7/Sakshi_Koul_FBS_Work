#to find the sum of three digit number
num=int(input("Enter a three digit number: "))

a=num%10
b=(num//10)%10
c=num//100
sum=a+b+c
print(f'The sum of the digits of {num} is {sum}')