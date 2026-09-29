# Calculator Project

# Import Calculator_Project_Art logo
import Calculator_Project_Art

# Step 1: Define basic math operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary mapping the symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Step 2: Main calculator function
def calculator():
    print(Calculator_Project_Art.logo)
    print("Welcome to the Calculator Project!\n")

    first_number = float(input("What's your first number?: "))
    should_continue = True

    while should_continue:
        # Display available operations
        for symbol in operations:
            print(symbol)

        symbol = input("What operation do you choose?: ")
        second_number = float(input("What's your next number?: "))

        # Perform calculations using the selected operation
        output = operations[symbol](n1 = first_number, n2 = second_number)
        print(f"{first_number} {symbol} {second_number} = {output}")

        # Ask user if they want to continue with the result
        continue_or_not = input(f"Type 'y' to continue calculating with {output}, "
                                f"or type 'n' to start a new calculation: ").lower()

        if continue_or_not == "y":
            first_number = output
        elif continue_or_not == "n":
            # Clear screen effect + restart the calculator
            should_continue = False
            print("\n" * 20)
            calculator()

# Step 3: Start the program
calculator()