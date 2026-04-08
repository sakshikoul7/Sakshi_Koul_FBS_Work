#Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition : a. Children below 12 = 30% discount b. Senior citizen (above 59) = 50% discount c. Others need to pay full.

n = int(input("Enter number of passengers: "))


cost = float(input("Enter cost per ticket: "))

total_amount = 0

# Loop for each passenger
for i in range(n):
    age = int(input(f"Enter age of passenger {i+1}: "))
    if age < 12:
        price = cost * 0.7   # 30% discount
    elif age > 59:
        price = cost * 0.5   # 50% discount
    else:
        price = cost         # full price

    total_amount += price

# Display total amount
print("Total ticket amount =", total_amount)