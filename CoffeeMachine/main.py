MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def are_resources_sufficient(drink_order):
    """checks if resources are sufficent to make drink, returns true or false"""
    for item in drink_order:
        if drink_order[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Calculate the total amount of coins"""
    print("Please insert coins")
    total = int(input("How many Quarters?")) * 0.25
    total += int(input("How many Dimes?")) * 0.1
    total += int(input("How many Nickels?")) * 0.05
    total += int(input("How many Pennies?")) * 0.01
    return total

def check_transaction_successful(drink_payment, drink_cost):
    if drink_payment >= drink_cost:
        change = round(drink_payment - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is your change of ${change}")
        return True
    else:
        print("Print sorry that is not enough Money")


def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
        print(f"Here is your {drink_name} ☕, Enjoy!")


still_on = True

while still_on:
    choice = input("What would you like? (espresso/latte/cappuccino): \n")
    print(choice)

    if choice == "off":
        still_on = False
        print("Goodbye, we hope to see you soon")

    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if are_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if check_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
#

#
