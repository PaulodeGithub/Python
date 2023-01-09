from art import logo


# calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    num1 = float(input("Choose a number?: "))
    for key in operations:
        print(key)
    operations_continue = True
    while operations_continue:
        symbol = input("Choose an operation from the symbols above: ")
        num2 = float(input("whats your next number?: "))
        calculation_function = operations[symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        if input(
                f"Type 'y' for more operations with {answer} or 'n' to start new calculation: "
        ) == "y":
            num1 = answer
        else:
            operations_continue = False
            calculator()


calculator()