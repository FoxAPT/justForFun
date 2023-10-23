#Highest Score

student_scores = input("Input a list of student scores:\n\n").split(",")

# Remove trailing commas from the values and convert to integers
student_scores = [int(score.rstrip(",")) for score in student_scores]

print("\n")

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score is {highest_score}!")

# Alternate way to check this using for loop is:

#print("\n")

# Find the maximum score
#max_score = max(student_scores)

# Print the maximum score
#print(f"The highest grade input is: {max_score}")

# Test numbers: 78, 65, 89, 86, 55, 91, 64, 89


