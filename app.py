print("Hello world!")

# Simple Python script that interacts with the user

def greet_user(name):
    """Function to greet the user"""
    print(f"Hello, {name}! Welcome to Python programming.")

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

# Main program
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet_user(user_name)

    # Taking two numbers as input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display result
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")

