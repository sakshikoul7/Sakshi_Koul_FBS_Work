#to check whether the triangle is equilateral, isosceles or scalene
a=float(input("Enter the length of the first side of the triangle: "))
b=float(input("Enter the length of the second side of the triangle: "))
c=float(input("Enter the length of the third side of the triangle: "))

if(a==b) and (b==c):
    print("The triangle is equilateral.")   
elif (a==b) or (b==c) or (a==c):
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")