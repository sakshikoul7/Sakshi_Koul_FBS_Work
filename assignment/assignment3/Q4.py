#to check whether the triangle is valid or not based on the lengths of its sides
a=float(input("Enter the length of the first side of the triangle: "))
b=float(input("Enter the length of the second side of the triangle: "))
c=float(input("Enter the length of the third side of the triangle: "))

if (a+b>c) and (a+c>b) and (b+c>a):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")