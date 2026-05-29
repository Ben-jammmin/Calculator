"""Simple calculator with basic arithmetic operations."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


print("Simple Python Calculator")
print("Operations: +, -, *, /")

while True:
    

    try:
        first = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second = float(input("Enter second number: "))

        if operator == "+":
            result = add(first, second)
        elif operator == "-":
            result = subtract(first, second)
        elif operator == "*":
            result = multiply(first, second)
        elif operator == "/":
            result = divide(first, second)
        else:
            raise ValueError("Unsupported operator")

        print(f"Result: {result}")
    except ValueError as exc:
        print(f"Error: {exc}")

    print("Would you like to perform another calculation? (yes/no)")
    answer = input().strip().lower()
    if answer == "yes":
        continue
    else: print("Goodbye!"); break   
    