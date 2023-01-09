
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
is_true = True




while is_true:
    options = menu.get_items()
    choice = input(f"What would you like to drink ({options})\n")
    if choice == "off":
        print("Goodbye")
        is_true = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)