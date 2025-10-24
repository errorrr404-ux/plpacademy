# Simple calculator program

# Ask the user for the first number
num1 = float(input("Enter the first number: "))

# Ask the user for the second number
num2 = float(input("Enter the second number: "))

# Ask the user to enter a mathematical operation
operation = input("Enter operation (+, -, *, /): ")

# Check which operation the user entered and perform it
if operation == '+':
    # If the operation is addition
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    # If the operation is subtraction
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    # If the operation is multiplication
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    # If the operation is division, check if divisor is not zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")

else:
    # If the operation entered is not one of the valid ones
    print("Invalid operation. Please use +, -, *, or /.")