#Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.
userid = "admin"
password = "admin123"
attempts = 3
while attempts > 0:
    user_input_id = input("Enter User ID: ")
    user_input_password = input("Enter Password: ")
    
    if user_input_id == userid and user_input_password == password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect credentials. You have {attempts} attempts left.")
else:
    print("Maximum attempts exceeded. Program terminated.")