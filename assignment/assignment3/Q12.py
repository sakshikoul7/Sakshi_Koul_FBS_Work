#to check if given 3 digit number is a palindrome or not

num=int(input("Enter a three digit number: "))

temp=num
d1=temp%10  
temp=temp//10 
d2=temp%10 
temp=temp//10 
d3=temp%10 

if(d1==d3):
    print(f'{num} is a palindrome number')
else:
    print(f'{num} is not a palindrome number')
