#input 5 subject marks from user and display grade
m1 = int(input("Enter the marks of Mathematics:"))
m2 = int(input("Enter the marks of English:"))
m3= int(input("Enter the marks of Science:"))
m4 = int(input("Enter the marks of Social Science:"))
m5 = int(input("Enter the marks of Hindi:"))

percentage = (m1 + m2 + m3 + m4 + m5)/500*100
if percentage>=90:
    print(f'Your percentage is {percentage}%. Your grade is A.')
elif percentage>=80:
    print(f'Your percentage is {percentage}%. Your grade is B.')
elif percentage>=70:
    print(f'Your percentage is {percentage}%. Your grade is C.')
elif percentage>=60:
    print(f'Your percentage is {percentage}%. Your grade is D.')
elif percentage>=50:
    print(f'Your percentage is {percentage}%. Your grade is E.')
else:
    print(f'Your percentage is {percentage}%. Your grade is F.')