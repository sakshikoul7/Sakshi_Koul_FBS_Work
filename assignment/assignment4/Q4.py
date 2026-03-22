#to print factorial of a number
num=int(input("Entet a number:"))
i=1
fact=1

while(i<=num):
    fact=fact*i
    i=i+1
print("Factorial:", fact)