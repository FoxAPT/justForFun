# FoxAPT (Wes Miller)
# COP2002-0T2
# Sept 24, 2023
# Project3.py
# This program allows a user to call vocabulary term definitions by inputing the number of the term listed.

def main():
    # Program terminology and definitions.
    program_terms = ['Algorithm', 'Variable', 'Variable Type (data type)', 'Array', 'If statement', 'Loop', 'Function', 'Class', 'Object', 'Method', 'Programming Language', 'Control Structure'] 

    program_definitions = [
    'is a set of instructions that are followed to solve a problem.',
    'container that holds a single number, word, or other information that you can use throughout a program.',
    'Basic variable types include: string (words and phrases), char (short for \'character;\' a single letter or symbol you can type), int (short for \'integer;\' for whole numbers), double or float (for decimal numbers), and bool (short for \'boolean;\' for true or false values.',
    'containers that hold variables of the same data type.', 
    'runs a block of code based on whether or not a condition is true.',
    'check a condition and then run a code block. The loop will continue to check and run until a specified condition is reached.',
    'block of code that can be referenced by name to run the code it contains.',
    'template definition of the methods and variables in a particular kind of object.', 
    'data type that has unique attributes and behavior.',
    'programmed procedure that is defined as part of a class and is available to any object instantiated from that class.', 
    'system of notation for writing computer programs.  Python is an example.', 
    'basic blocks for decision making processes in computing.'] 
     
    # Prompt user to to enter the number of a term. 
    print("This program will provide definitions to important programming terms.\nChoose a number to see the term's definition.\n\nTerms:")

    count = 0
    
    # Loop through terms and print the selected term.
    for x in program_terms:
      count = count + 1
      print(str(count) + ".  " + str(x)) 

    print()
    
    selected_number = int(input("Enter the number of the term you want:  "))

    # Print the selected terms definition if the number is valid, otherwise print an error statement.
    if selected_number > 0 and selected_number < 13:
     print("\n" + program_terms[selected_number - 1] + ":  " + program_definitions[selected_number - 1])
    else:
     print("\nError! Not a valid choice.")
     
if(__name__=="__main__"):
  main()
