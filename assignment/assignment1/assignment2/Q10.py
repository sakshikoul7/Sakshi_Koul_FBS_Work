#to reverse a three digit number
num=int(input("Enter a three digit number:"))

a=num%10
b=num//10
c=b%10
d=num//100
reverse=(a*100)+(c*10)+d
print(f'The reverse of {num} is {reverse}')