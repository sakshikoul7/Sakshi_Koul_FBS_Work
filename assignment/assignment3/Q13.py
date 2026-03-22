#to input electricity unit consumed and calculate the total electricity bill based on the given conditions
units=int(input("Enter the electricity units consumed: "))
if units<=50:
    bill=units*0.50
elif units<=150:
    bill=units*0.75
elif units<=250:
    bill=units*1.20
else:
    bill=units*1.50
surcharge=0.20*bill
total_bill=bill+surcharge
print(f'The total electricity bill is {total_bill}')