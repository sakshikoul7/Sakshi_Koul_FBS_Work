#to calculate salary of an employee based on basic , da=10% of basic, ta = 12% of basic and hra=15% of basic

basic=float(input("Enter the basic salary of the employee: "))
da=0.1*basic
ta=0.12*basic
hra=0.15*basic

gross_salary=basic+da+ta+hra
print(f'The gross salary of the employee is {gross_salary}')