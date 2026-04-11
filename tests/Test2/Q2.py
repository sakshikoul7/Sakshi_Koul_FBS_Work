#to accept 3 digit number. If first digit id double of second digit and half of third digit then display "Yes, you have done it", otherwise display "Please try next time"
num= int(input("Enter a 3 digit number: "))
a=num//100
b=(num//10)%10
c=num%10

if a==2*b and a==c/2:
    print("Yes, you have done it")
else:
    print("Please try next time")