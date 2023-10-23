#Who’s Paying?


import random


person_who_pays = input("Type in everyones name to see who goes first! ")


#Split string method allows you to create a list using commas.
names = person_who_pays.split(", ")

# len will give you the number of items in the list or number of letters in a string. In order to complete our algorithm we have to create a bridge between len and num_items by assigning a variable for it to work.
num_items = len(names)

# To obtain an unpredictable number of items in a list you need to remember python starts counting at 0 whereas len starts counting at 1. So we use num_items - 1 to obtain the correct count for python.

person_who_pays = random.choice(names)

print("\n")
print(person_who_pays + " is buying! ")

