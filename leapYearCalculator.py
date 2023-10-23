#Leap Year Calculator


#Using code to check if a year is a leap year or not.
#This math is based on if a year is evenly divisible by 4 it is a leap year, except every year which is also divisible by 100. Unless the year is also evenly divisible by 400.

year = int(input("Which year do you want to check? "))

if year % 4 == 0 and (year % 100!= 0 or year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")

# Alternate way to code the above would be as follows: 

year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Leap year.")
  else:
    print("Leap year.")
else: 
  print("Not a leap year")

