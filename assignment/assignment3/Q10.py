#to check whether the person is eligible for marriage or not based on his/her age
gender=input("Enter your gender:")
age=int(input("Enter your age: "))

if (gender in ['female', 'F', 'f', 'Female', 'FEMALE']):
    if age>=18:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")
else:
    if age>=21:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")
    
               