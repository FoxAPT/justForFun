#PyPizza

# Python Pizza Ordering Algorithm.

print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, L?: ")
add_pepperoni = input("Do you want pepperoni ? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# Sizes of Pizzas == cost.
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

# Adding toppings.
if add_pepperoni == "Y":
  if size == "S":
    #Nesting an "if" statement within another "if" statement adds a condition in which it must meet."
    bill += 2
  else: 
    bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is {bill}, thank you for ordering python pizza!")

