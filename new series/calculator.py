# Simple Calculator in Python

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Main program
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is one of the options
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

    else:
        print("Invalid Input")

    # Ask if user wants to perform another calculation
    next_calculation = input("Do you want to perform another calculation? (1/0): ")
    if next_calculation.lower() != '1':
        print("Thank you for using the calculator")
        break
        
# Function to perform power calculation
def power(x, y):
    return x ** y

# Update the main program
print("5. Power")

# Update the while loop
while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5): ")

    # Check if the choice is one of the options
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # ... (previous code for choices 1-4)

    elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")

    else:
        print("Invalid Input")

    # ... (rest of the code remains the same)
