# Functions Calculator

### This function adds two numbers.

```commandline
def add(num1: int, num2: int):
    return num1 + num2
```

### This function subtracts two numbers.

```commandline
def subtract(num1: int, num2: int):
    return num1 - num2
```

### This function multiplies two numbers.
```commandline
def multiply(num1: int, num2: int):
    return num1 * num2
```

### This function divides two numbers.
```commandline
def divide(num1: int, num2: int):
    return num1 / num2
```

### Tells the user which operators they can select from.

```commandline
print("Select the operation")
print("a - Add")
print("b - Subtract")
print("c - Multiply")
print("d - Divide")
```

### Let the user choose which operator they want to pick.

```commandline
operation = input("Your choice of operation: ")
```

### Let the user input two different numbers.

```commandline
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))
```

### Depending on which operator the user chooses, there are different functions that can happen.

```commandline
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
```
