#to find roots of a quadratic equation

a=float(input("Enter the coefficient of x^2: "))
b=float(input("Enter the coefficient of x: "))
c=float(input("Enter the constant term: "))

d = b**2 - 4*a*c

r1 = (-b + d**0.5) / (2*a)
r2 = (-b - d**0.5) / (2*a)

print(f'The roots of the quadratic equation are {r1} and {r2}')