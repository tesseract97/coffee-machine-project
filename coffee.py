import json

import menu


def start_coffee_machine():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        if 'money' not in menu.resources:
            menu.resources['money'] = 0.00
        print(f"Water: {menu.resources['water']}ml\nMilk: {menu.resources['milk']}ml\n"
              f"Coffee: {menu.resources['coffee']}g\nMoney: ${menu.resources['money']}")
    elif order == "off":
        exit()
    elif order in ["latte", "cappuccino", "espresso"]:
        code, product = check_resources(order)
        if code:
            print(f"Sorry there is not enough {product}")
        else:
            code, change = process_coins(order)
            if not code:
                print("stopping point")
    # TODO: deduct from resources
    else:
        print("Sorry, that isn't on the menu. Please order again")
    start_coffee_machine()


def make_coffee(order):
    print(order)


def check_resources(order):
    for i in menu.MENU[order]["ingredients"]:
        if menu.MENU[order]["ingredients"][i] > menu.resources[i]:
            return 1, i
    return 0, 0


def process_coins(order):
    print("Please insert coins to pay for your order")
    try:
        quarters = int(input("Please insert number of quarters: "))
        dimes = int(input("Please insert number of dimes: "))
        nickels = int(input("Please insert number of nickels: "))
        pennies = int(input("Please insert of pennies: "))
        value = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
        if value > menu.MENU[order]['cost']:
            change = value - menu.MENU[order]['cost']
            return 0, change
        else:
            print("Sorry that's not enough money. Money refunded.")
            return 1, 0
    except ValueError as e:
        print("Please enter your coin values again")
        process_coins(order)


if __name__ == '__main__':
    start_coffee_machine()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
