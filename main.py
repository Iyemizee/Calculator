from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    continue_calc = True
    while continue_calc:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation.: ").lower()
        if continue_calculation == "y":
            num1 = result
        else:
            continue_calc = False
            '''recursion:  called the calculator function inside the function to begin a fresh calculation'''
            calculator()
calculator()