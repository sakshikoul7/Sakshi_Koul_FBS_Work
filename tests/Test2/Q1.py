#To accept year from user and check whether it is a leap year or not
year=int(input("Enter a year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")