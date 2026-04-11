#to calculate total bill after adding 18% GST. He buys 5 products. Accpt price of each product from user.
total_bill = 0
gst_rate = 0.18
for i in range(1, 6):
    price = float(input(f"Enter the price of product {i}: "))
    total_bill = total_bill+ price
total_bill_with_gst = total_bill + (total_bill * gst_rate)
print(f"Total bill after adding 18% GST: {total_bill_with_gst}")    
