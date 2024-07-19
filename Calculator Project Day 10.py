# All functions listed below. 
def clear():
    print("\n"*50)

# add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1* n2

# Divide
def divide(n1, n2):
    return n1/n2

# The different types of operations you can preform on this calculator
operatations = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide
}
def calculator():
    total = 0
    answer = 'y'
    num1 = float(input("What's the first number?: "))
    while answer == 'y':
        for operation in operatations:
            print(operation)

        their_choice = input("Pick a operation: ")
        num2 = float(input("What's the next number?: "))

        if their_choice == "+":
            total = add(num1, num2)
            print(f"{num1} + {num2} = {total} ")

        elif their_choice == "-":
            total = subtract(num1, num2)
            print(f"{num1} - {num2} = {total} ")

        elif their_choice == "*":
            total = multiply(num1, num2)
            print(f"{num1} * {num2} = {total} ")

        elif their_choice == "/":
            total = divide(num1, num2)
            print(f"{num1} / {num2} = {total} ")

        num1 = total

        answer = (input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")).lower()
    if answer == "n":
        clear()
        # Using recursion to create a new calculation.
        calculator()
calculator()


