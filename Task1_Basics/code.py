# Task 1: Python Calculator with Logging
# Intern: Swasthik Servegar
# Date: 22 Sept 2025

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

def log_operation(operation, a, b, result):
    with open("log.txt", "a") as file:
        file.write(f"{operation}: {a} & {b} = {result}\n")

print("Welcome to Python Calculator!")
print("Operations: add, subtract, multiply, divide")

while True:
    op = input("Enter operation (or 'exit' to quit): ").lower()
    if op == "exit":
        print("Thank you for using the calculator!")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == "add":
        res = add(a, b)
    elif op == "subtract":
        res = subtract(a, b)
    elif op == "multiply":
        res = multiply(a, b)
    elif op == "divide":
        res = divide(a, b)
    else:
        print("Invalid operation! Try again.")
        continue

    print(f"Result: {res}")
    log_operation(op, a, b, res)

