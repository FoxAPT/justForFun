# Define a list of questions.
questions = [
    "Given the bolded text of It's James!, how many characters are needed to represent this string?",
    "Which of the following is a good idea if you get an index error and can't figure out what to do to fix it?  Choose ALL which apply..",
    "Suppose I have a list called listOfNames with the following elements:\n\"James\"\n\"Elisabeth\"\n\"Omar\"\n\"Joe\"\n\"Janice\"\n\"Trisha\"\n\"Cole\"\n\"Kevin\"\n\"Jenn\"\n\"Olivia\"\nSuppose I want to get the value of \"Omar\".  What would the code snippet look like to access this value making sure to use a positive value?",
    "Suppose I have a list called myAttendees, but because values have been added and removed during program execution, I don't know how many items are in it.\nWhat would the code snippet look like to access the last value in this list making sure to use a positive value for the index value?",
    "Suppose I have a list called myAttendees.  I want to know the size of this list.  What would this code snippet look like to do this?",
    "Suppose I have the following snippet of code:\nbookName=\"Puns created by james\"\nbookName=*****Inserted code********\nprint(bookName)\nWhat code would I use to replace *****Inserted code******** to have it print the text Puns Created By James?"
]

# Define a list of selected answers.
selected_exam_answers = [
    "Why is the answer '11' an incorrect answer?",
    "Why is 'Try printing a different list' an incorrect answer? I feel that this could be a valid way of troubleshooting an issue.",
    "Please explain why '[name=listOfNames[2]' is incorrect code.",
    "Please explain why 'lastValue=myAttendees[-1]' is incorrect code.",
    "Please explain why 'listSize=len(myAttendees)' is incorrect code.",
    "Please explain why 'bookName=bookName.title()' is incorrect code."
]

# List of incorrect question numbers.
incorrect_question_numbers = [3, 13, 15, 18, 19, 21]

# Flag to control the loop.
keep_running = True

# Get user input for the question number to check.
while keep_running:
    try:
        question_number = int(input("Enter a question number from the list [3, 13, 15, 18, 19, 21] (or -1 to quit): "))
        if question_number in incorrect_question_numbers:
            question_index = incorrect_question_numbers.index(question_number)
            print(f"\nQuestion {question_number}: {questions[question_index]}")
            print(f"\nSelected Answer: {selected_exam_answers[question_index]}\n")
        elif question_number == -1:
            print("\nGoodbye!")
            keep_running = False
        else:
            print("Invalid input. Please enter a number from the list [3, 13, 15, 18, 19, 21] or -1 to quit.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
