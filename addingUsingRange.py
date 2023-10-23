#Let’s Add 1, 100 using Range!

#For Loops with Lists. Remember with ranges if you want to count from 1, 10 python will only give you 1, 9. In order to get 10 you have to set range 1 number above for ex: 1, 11.
#for number in range(1, 11, 3):
#  print(number)
  # You can also have the range increase step by a number by following a range with a number for ex: range(1, 11, 3) which will print: 1, 4, 7 etc.

total = 0
for number in range(1, 101):
  total += number
print(total)

Sub Challenge: Add all even numbers 1, 100 using For Loop and Range.

total = 0
for number in range(2, 101, 2):
  total += number
print(total)

# Indentation is important because if it is inside of the for loop it will print every step of the calculation.
  


