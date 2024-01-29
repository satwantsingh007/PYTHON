from ingredients import MENU, resources

profit = 0


def is_ingredient_enough(order_ingredients):
    for items in order_ingredients:
        if resources[items] <= order_ingredients[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def process_coins():
    print('Please Insert Coins.')
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)


def is_transaction_successfully(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredient, drink_name):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}☕")


proceed = True
while proceed:
    customer_choice = input(" What would you like? (espresso/latte/cappuccino): ")
    if customer_choice == 'off':
        proceed = False
    elif customer_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[customer_choice]
        if is_ingredient_enough(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successfully(payment, drink['cost']):
                make_coffee(drink['ingredients'], customer_choice)
