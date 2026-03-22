#to check whether the user has entered a valid userid and password or not and display a 4 digit otp and ask the user to enter that otp if the userid and password are valid
userid=input("Enter your userid: ")
password=input("Enter your password: ")
if userid=="sakshi.koul__" and password=="sakshi123":
    print("You have entered a valid userid and password.")
    import random
    otp=random.randint(1000,9999)
    print(f'Your OTP is {otp}')
    user_otp=int(input("Enter the OTP: "))
    if user_otp==otp:
        print("OTP is correct. You have successfully logged in.")
    else:
        print("OTP is incorrect. Please try again.")
else:
    print("You have entered an invalid userid or password.")