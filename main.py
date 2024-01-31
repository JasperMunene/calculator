def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

# Main function to take user input and perform calculations
def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the operation number (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

    else:
        print("Invalid input. Please enter a valid operation number.")

# Run the calculator
calculator()