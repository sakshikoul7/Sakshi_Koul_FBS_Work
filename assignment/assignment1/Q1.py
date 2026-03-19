#percentage of student based on marks of any 5 subjects
m1=float(input("Enter the marks of English:"))
m2=float(input("Enter the marks of Mathematics:"))
m3=float(input("Enter the marks of Science:"))
m4=float(input("Enter the marks of Social Science:"))
m5=float(input("Enter the marks of Hindi:"))

percentage = ((m1+m2+m3+m4+m5)/500)*100

print(f'The percentage of student is {percentage}%')