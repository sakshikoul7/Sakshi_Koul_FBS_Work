#to calculate selling price of book based on cost price and discount
cp=float(input("Enter the cost price of the book: "))
d=float(input("Enter the discount percentage: "))

discount= (cp*d)/100
sp=cp-discount

print(f'The selling price of the book is {sp}')

