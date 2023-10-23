# FoxAPT (Wes Miller)
# COP2002-0T2
# Sept 24, 2023
# Project3.py
# This program allows a user to call vocabulary term definitions by inputing the number of the term listed.

def main():
    # Defining dictionary with programming terms and their definitions.
    programming_terms = {
        1: "Algorithm: is a set of instructions that are followed to solve a problem.",
        2: "Variable: container that holds a single number, word, or other information that you can use throughout a program.",
        3: "Variable Type (data type): Basic variable types include: string (words and phrases), char (short for 'character;' a single letter or symbol you can type), int (short for 'integer;' for whole numbers), double or float (for decimal numbers), and bool (short for 'boolean;' for true or false values.",
        4: "Array: containers that hold variables of the same data type.",
        5: "If statement: runs a block of code based on whether or not a condition is true.",
        6: "Loop: check a condition and then run a code block. The loop will continue to check and run until a specified condition is reached.",
        7: "Function: block of code that can be referenced by name to run the code it contains.",
        8: "Class: template definition of the methods and variables in a particular kind of object.",
        9: "Object: data type that has unique attributes and behavior.",
        10: "Method: programmed procedure that is defined as part of a class and is available to any object instantiated from that class.",
        11: "Programming Language: system of notation for writing computer programs. Python is an example.",
        12: "Control Structure: basic blocks for decision-making processes in computing."
    }

    print("""
    1. Algorithm
    2. Variable
    3. Variable Type (data type)
    4. Array
    5. If statement
    6. Loop
    7. Function
    8. Class
    9. Object
    10. Method
    11. Programming Language
    12. Control Structure""")
    
    continue_loop = True
    
    while continue_loop:
        # Ask the user to choose a term
        choice = input("\nEnter the number of a term for its definition (enter '0' to exit): ")
        
        if choice == '0':
            continue_loop = False  # Exit the program if the user enters '0'
        else:
            try:
                choice = int(choice)
                if choice in programming_terms:
                    # Display the selected term's definition
                    print(f"\nDefinition of Term {choice}:\n")
                    print(programming_terms[choice])
                else:
                    print("\nError! Not a valid choice.")
            except ValueError:
                print("\nError! Please enter a valid number.")

if __name__ == "__main__":
    main()
  
