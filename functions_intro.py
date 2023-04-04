# Functions

# Allow you to follow DRY
# DRY - Do Not Repeat Yourself

# def print_something():  # def - Define  # print_somthing(): - Name of method
#     print("something has been printed")
#
# print_something()  # Calling the function

def print_something(print_string):
    print(print_string)

print_something("My name is Samuel")
print_something("My second name is Naiwo")

def greeting(name):
    print("Hello, my name is " + name)

greeting("Samuel")

# Return Statement (use return as default)
def addition(int1, int2):
    return int1 + int2

print(addition(2, 2))

# Default Arguments (two)
def addition(int3=3, int4=3):  # Has a default set but can be changed.
    return int3 + int4

print(addition(10, 2))

# Multiple Arguments
def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 2, 3, 3, 4, 5, 6)

# Type Hints
def greeting(name: str):
    print("Hello, my name is " + name)

greeting("Samuel")

def division(denum: int, num: int) -> float:  # Tells what we are expecting as an output.
    return denum / num

print(division(12, 5))

# This function subtracts two numbers
def subtraction (int1: int = 5, int2: int = 2) -> int:
    return int1 - int2

print(subtraction())

# Functions best practices
# 1. Name your methods using lowercase and underscores
# 2. All arguments should be clear in their need and where possible their expected type.
# 3. Remember the return statement or it will return None.
# 4. Keep functions as small as possible.
# 5. Use comments within your methods to help with instructions.
# 6. Consider using type hints to avoid errors earlier.