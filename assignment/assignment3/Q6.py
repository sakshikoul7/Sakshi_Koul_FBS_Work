#to calculate profit or loss based on cost price and selling price
cp=float(input("Enter the cost price of the item: "))
sp=float(input("Enter the selling price of the item: "))

if sp>cp:
    profit=sp-cp
    print(f'The profit is {profit}')
elif sp<cp:
    loss=cp-sp
    print(f'The loss is {loss}')
else:
    print("There is no profit or loss.")