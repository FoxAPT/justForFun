ROCK, PAPER, SCISSORS







import random
# Here we have imported our random condition which will be applied to the computer_choice variable.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
# The list above allows us to use the list within a variable which will make it easier to apply and develop if we needed to at a later time. We also us this list as a form of output being that the list begins at the number 0, and counts up to 2.

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n\n"))

if user_choice < 0 or user_choice > 2: 
  print("\n")
  print("You typed an invalid number, you lose!") 
# When applying rules of invalidation, the rules must be applied above the rest of the code so it will check and validate whether an answer was correctly input or not.
else:
  print(game_images[user_choice])
# By applying the (game_images[user_choice]) variables we are able to appropriately print images by pulling them from the list when  we have applied the users choice variable.This same concept will be applied to the computer_choice variable but it will be random.

  print("\n")

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])



  if user_choice == 0 and computer_choice == 2:
      print("You win!")
  elif computer_choice == 0 and user_choice == 2:
      print("You lose")
  elif computer_choice > user_choice:
      print("You lose")
  elif user_choice > computer_choice:
      print("You win!")
  elif computer_choice == user_choice:
      print("It's a draw")

