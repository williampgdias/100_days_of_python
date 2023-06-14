print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? €"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_to_split = int(input("How many people to split the bill? "))

bill_with_tip = tip_percentage / 100 * total_bill + total_bill
bill_per_person = bill_with_tip / people_to_split
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: €{final_amount}")

# tip_amount = total_bill * (tip_percentage / 100)
# total_amount = total_bill + tip_amount
# amount_per_person = total_amount / people_to_split

# print(f"Each person should pay: {amount_per_person:.2f}")