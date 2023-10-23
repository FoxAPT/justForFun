#Average Student Heights

student_heights = input("Input a list of student heights:\n\n").split()

# Remove trailing commas from the values
student_heights = [height.rstrip(",") for height in student_heights]

for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)


#print(student_heights)
print("Student Heights you have input.\n\n")

print(total_height)
print("Sum of the student's heights. \n\n")

print(number_of_students)
print("Number of students. \n\n")

print(average_height)
print("Average height of students. \n\n")

# Test Heights 180, 124, 165, 173, 189, 169, 146

