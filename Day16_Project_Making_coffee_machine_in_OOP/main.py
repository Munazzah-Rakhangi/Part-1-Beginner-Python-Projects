from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()  #Object is MoneyMachine.
my_coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# my_money_machine.report()
# my_coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like ? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_money_machine.report()
        my_coffee_maker.report()
    else:
        drink = menu.find_drink(order_name=choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(cost = drink.cost):
            my_coffee_maker.make_coffee(order=drink)
            