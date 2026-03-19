#to swap two numbers without using a temporary variable
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

a=a+b
b=a-b
a=a-b
print(f'After swapping, the first number is {a} and the second number is {b}')