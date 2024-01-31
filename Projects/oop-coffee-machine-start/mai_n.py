from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

proceed = True
while proceed:
    customer_choice = input(f" What would you like? {menu.get_items()}: ")
    if customer_choice == 'off':
        proceed = False
    elif customer_choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(customer_choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
