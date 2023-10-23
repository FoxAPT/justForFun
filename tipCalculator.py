#Tip Calculator

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("How much would you like to tip? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
# Alternate ways to accomplish the tasks above.
# bill_with_tip = tip / 100 * bill + bill
       # or 
# Alternate ways of doing this would b: bill_with_tip = bill * (1 + tip /100) 

final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
# Using the {:.2f}.format function is what gives us the $33.60 format instead of $33.6 format.

