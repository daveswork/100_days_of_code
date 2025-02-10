
import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

print(operations["*"](4,8))

continuation = "n"

while True:
    if continuation == "n":
        print(art.logo)
        first_number = float(input("What is the first number?: "))
    operator = input("+\n-\n*\n/\nPick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = operations[operator](first_number, second_number)
    print(f"{first_number} {operator} {second_number} = {result}")
    continuation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if continuation == "y":
        first_number = result

