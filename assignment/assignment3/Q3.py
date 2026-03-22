#to check whether the triangle is valid or not based on the sum of its angles
a=float(input("Enter the first angle of the triangle: "))
b=float(input("Enter the second angle of the triangle: "))
c=float(input("Enter the third angle of the triangle: "))

angle=a+b+c

if(angle==180):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")