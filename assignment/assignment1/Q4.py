#to calculate simple interest

principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time in years: "))

si = (principal*rate*time)/100
print(f'The Simple Interest is {si}')