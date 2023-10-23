def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

while True:
    num1 = float(input("What's the first number? "))
    print("\n")

    for symbol in operations:
        print(symbol)

    print("\n")
    operation_symbol = input("Pick an operation from the line above (or type 'exit' to quit): ")

    if operation_symbol.lower() == "exit":
        print("\nGoodbye! Calculator has been exited.")
        break

    print("\n")
    num2 = float(input("What's the second number? "))

    calculation_function = operations.get(operation_symbol)

    if calculation_function:
        first_answer = calculation_function(num1, num2)
        print("\n")
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        print("\n")
    else:
        print("\nInvalid operation symbol. Please try again.\n")
        continue

    while True:
        operation_symbol = input("Pick another operation (or type 'exit' to quit): ")

        if operation_symbol.lower() == "exit":
            break  # Break out of the inner loop

        print("\n")
        num3 = float(input("What's the next number? "))

        calculation_function = operations.get(operation_symbol)

        if calculation_function:
            second_answer = calculation_function(first_answer, num3)
            print("\n")
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
            print("\n")
            first_answer = second_answer
        else:
            print("\nInvalid operation symbol. Please try again.\n")

    else:
        continue  # Continue the outer loop

    break  # Only executed if the inner loop is exited with "exit"

print("\nGoodbye! Calculator has been exited.")
