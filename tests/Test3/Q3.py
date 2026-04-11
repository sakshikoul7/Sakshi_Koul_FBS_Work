#Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. Based on this calculate the total salary of each emp and also total salary of all emp.
n=int(input("Enter number of employees:"))
total_salary=0
for i in range(n):
    basic_salary=int(input("Enter basic salary of employee:"))
    if basic_salary<20000:
        da=0.1*basic_salary
        ta=0.12*basic_salary
        hra=0.15*basic_salary
    else:
        da=0.15*basic_salary
        ta=0.18*basic_salary
        hra=0.2*basic_salary
    total_salary_employees=basic_salary+da+ta+hra
    print("Total salary of employee",i+1,"is:",total_salary_employees)
    total_salary+=total_salary_employees
print("Total salary of all employees is:",total_salary)