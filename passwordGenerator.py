#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! \n\n")

print("NOTE: Never reuse  a password for more than one account. It makes your accounts accessible to threat actors. \n\n")
nr_letters= int(input("How many letters would you like in your password? \n\n")) 
print("\n")

nr_symbols = int(input(f"How many symbols would you like? \n\n"))
print("\n")

nr_numbers = int(input(f"How many numbers would you like? \n\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))


for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))


for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char 

print("\n")
print(f"Your password is: \n\n {password}")

