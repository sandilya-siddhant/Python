#Tip Calculator

#Ask the User For The Bill Amount
bill_amount=float(input("Enter the total bill amount :"))

#Ask the User For The Bill Percentage
tip_percentage=float(input("Enter the tip percentage :"))

#Calculate the tip amount
tip_amount=(tip_percentage/100)*bill_amount

#Calculate the total amount (bill+tip)
total_amount=bill_amount+tip_amount

#Print the results
print(f"\nThe tip amount is:₹{tip_amount:.2f}")
print(f"The total bill amount including tip is: ₹{total_amount:.2f}")
