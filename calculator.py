def start():
    while True:
        print(""" 
            Welcome to the calculator 
            1. press + to add
            2. press - to subtract
            3. press * to multiply
            4. press / to divide
        """)  
        calculator_inputs()

        # Ask the user if they want to perform another calculation
        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break  # Exit the loop and end the program
1
def calculator_inputs():
    num1 = validate_number("Enter the first number: ")
    operation = validate_operation()  # Validate operation
    num2 = validate_number_for_division("Enter the second number: ", operation)
    calculator(num1, operation, num2)

def calculator(num1, operation, num2):
    # Perform the operation based on user input
    if operation == '+':
        result = num1 + num2
        print(f"The result is: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result is: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result is: {result}")
    elif operation == '/':
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Invalid operation.")

def validate_operation():
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def validate_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def validate_number_for_division(prompt, operation):
    while True:
        num = float(input(prompt))
        if operation == '/' and num == 0:
            print("Error: Division by zero is not allowed. Please enter a non-zero number.")
        else:
            return num


def allocate():
    start=input("")

start()
