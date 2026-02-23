 #Accept price input for 3 different items
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

# Calculate total cost
total = item1 + item2 + item3

# Apply discount if total exceeds $50
if total > 50:
    discount = total * 0.10
else:
    discount = 0

# Calculate final payable amount#
final_amount = total - discount

# Display results
print("Original Total: $", total)
print("Discount Amount: $", discount)
print("Final Payable Amount: $", final_amount)