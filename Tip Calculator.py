#Tip Calculator

bill_amount=float(input("Enter the total bill amount :"))

tip_percentage=float(input("Enter the tip percentage :"))

tip_amount=(tip_percentage/100)*bill_amount

total_amount=bill_amount+tip_amount

print(f"\nThe tip amount is:₹{tip_amount:.2f}")
print(f"The total bill amount including tip is: ₹{total_amount:.2f}")
