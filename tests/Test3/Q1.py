#Write a program to print first n prime numbers
num=int(input("Enter the number of prime numbers to print:"))
count=0
for i in range(2,num):
    for j in range(2,i):
        if(i%j)==0:
            break
    else:
        print(i)
        count+=1
        if(count==num):
            break