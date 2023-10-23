print("Welcome to the Love Calculator!")
# Establish your variables.
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

# Establish your calculations, separate each letter so you can calculate them individually then add them up within a mathmatical equation.
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e

# Convert integers into str format so you can calculate, int and str cannot work together.
love_score = str(true) + str(love)
# Convert variable into an int so it can be calculated and applied to your code.
love_score = int(love_score)


if love_score < 10 or love_score > 90:
  #You may choose to wrap conditions in parentheses but do not have to. It may make it easier to read for some programmers.
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 10 and love_score <= 50:
  print(f"Your love score is {love_score}, you are alright together.")
elif love_score >= 50 and love_score <= 90:
  print(f"Your love score is {love_score}, you have a solid foundation.")
else:
  print(f"Your love score is {love_score}.")
# Separating percentages to identify specific scores is useful for establishing levels of compatability.
