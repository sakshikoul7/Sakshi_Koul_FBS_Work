#to accept age of five people and also per person ticket amount and then calculate total amount of ticket \

age1=int(input("Enter the age of the first person: "))
age2=int(input("Enter the age of the second person: "))
age3=int(input("Enter the age of the third person: "))
age4=int(input("Enter the age of the fourth person: "))
age5=int(input("Enter the age of the fifth person: "))
ticket_amount=float(input("Enter the ticket amount per person: "))

if age1<12:
    amt1 = ticket_amount-(0.30*ticket_amount)
elif age1>59:
    amt1 = ticket_amount-(0.50*ticket_amount)
else:
    amt1 = ticket_amount

if age2<12:
    amt2 = ticket_amount-(0.30*ticket_amount)
elif age2>59:
    amt2 = ticket_amount-(0.50*ticket_amount)
else:
    amt2 = ticket_amount

if age3<12:
    amt3 = ticket_amount-(0.30*ticket_amount)
elif age3>59:
    amt3 = ticket_amount-(0.50*ticket_amount)
else:
    amt3 = ticket_amount

if age4<12:
    amt4 = ticket_amount-(0.30*ticket_amount)
elif age4>59:
    amt4 = ticket_amount-(0.50*ticket_amount)
else:
    amt4 = ticket_amount

if age5<12:
    amt5 = ticket_amount-(0.30*ticket_amount)
elif age5>59:
    amt5 = ticket_amount-(0.50*ticket_amount)
else:
    amt5 = ticket_amount

total_amount=amt1+amt2+amt3+amt4+amt5
print(f'The total amount of the ticket is {total_amount}')