#to calculate compound interest
principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time in years: "))

ci = principal * ((1 + rate / 100) ** time) - principal
print(f'The Compound Interest is {ci}')
