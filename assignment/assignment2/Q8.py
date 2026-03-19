#to swap two numbers using third variable
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

temp=a
a=b
b=temp
print(f'After swapping, the first number is {a} and the second number is {b}')
