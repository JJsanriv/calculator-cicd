import math

"""Simple calculator module to demonstrate CI/CD."""

def add(a:  float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b:  float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a: float, b: float) -> float:
    """Exponentation of two numbers"""
    if b < 0:
        raise ValueError("Exponent cannot be less than 0")
    elif b == 0:
        return 1
    return a ** b

def root(a: int) -> float:
    """Any root of a number"""
    return math.sqrt(a)

if __name__ == "__main__":
    
    x = input("Select a function: \n- 'a' for Add\n- 'b' for Substraction\n- 'c' for Multiplication\n- 'd' for Division\n- 'e' for Exponentation\n- 'f' for Square root\nYour selection: ")
    
    if x != 'a' or 'b' or 'c' or 'd' or 'e':
        print("Incorrect input! Try again")

    match x:
        case 'a':
            print("You selected Add! Select two numbers")
            y = input("First number is ")
            z = input("Second number is ")
            n = add(float(y),float(z))
            print(f"The result is -->", n)
        case 'b':
            print("You selected Subtract! Select two numbers")
            y = input("First number is ")
            z = input("Second number is ")
            n = subtract(float(y),float(z))
            print(f"The result is -->", n)
        case 'c':
            print("You selected Multiplication! Select two numbers")
            y = input("First number is ")
            z = input("Second number is ")
            n = multiply(float(y),float(z))
            print(f"The result is -->", n)
        case 'd':
            print("You selected Division! Select two numbers")
            y = input("First number is ")
            z = input("Second number is ")
            n = divide(float(y),float(z))
            print(f"The result is -->", n)
        case 'e':
            print("You selected Exponentation! Select two numbers")
            y = input("First number is ")
            z = input("Second number is ")
            n = pow(float(y),float(z))
            print(f"The result is -->", n)
        case 'f':
            print("You selected Square root! Select two numbers")
            y = input("The number is ")
            n = root(int(y))
            print(f"The result is -->", n)
    
    
