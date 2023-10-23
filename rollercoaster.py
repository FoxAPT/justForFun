Rollercoaster! 


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("you can ride the rollercoaster.")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7
    print("Please pay $7.")
  elif age > 55:
    print("Save your money for a headstone.")
  else:
    bill = 12
    print("Please pay $12.")

  wants_photo = input("Do you want a photo taken? Y or N? ")
  if wants_photo == "y" or "Y":
    bill += 3
else:
  print("Sorry, you have to grow taller before you can ride.")
  
print(f"Your final bill is ${bill} ")
  
#Utilizing “if” condition on multiple lines allows more than one to be used; whereas using if, elif, and else only allows one condition to be used. When using "if, elif, else" condition you must pair them together or they will not function properly.
