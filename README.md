# mino.py
This is a minifier for python
<br>
No adittional libraries are required
<br>
To use do `python mino.py <filename>`
_________
Examples
--------
Before minifaction:
``` python
# This is a basic calculator program in Python

# Function to add two numbers
def add(num1, num2):
    # The '+' operator is used to add two numbers
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    # The '-' operator is used to subtract two numbers
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    # The '*' operator is used to multiply two numbers
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    # The '/' operator is used to divide two numbers
    # We need to handle the case where num2 is zero to avoid division by zero error
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return num1 / num2

# Main function to take user input and perform calculations
def main():
    # Print a welcome message
    print("Welcome to the calculator program!")

    # Take input from the user
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation based on the operator entered by the user
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "Error! Invalid operator."

    # Print the result
    print("The result is:", result)

# Call the main function
if __name__ == "__main__":
    main()
```
_________
After minifaction:
``` python
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return 'Error! Division by zero is not allowed.'
    else:
        return num1 / num2
def main():
    print('Welcome to the calculator program!')
    num1 = float(input('Enter first number: '))
    operator = input('Enter operator (+, -, *, /): ')
    num2 = float(input('Enter second number: '))
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        result = 'Error! Invalid operator.'
    print('The result is:', result)
if __name__ == '__main__':
    main()
```
