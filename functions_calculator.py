# Make a calculator using functions.

def add(num1: int, num2: int):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


def divide(num1: int, num2: int):
    return num1 / num2

print("Select the operation")
print("a - Add")
print("b - Subtract")
print("c - Multiply")
print("d - Divide")

operation = input("Your choice of operation: ")

number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))

if operation == "a":
    print(number_1 + number_2)
elif operation == "b":
    print(number_1 - number_2)
elif operation == "c":
    print(number_1 * number_2)
elif operation == "d":
    print(number_1 * number_2)
else:
    print("Invalid input, please try again")