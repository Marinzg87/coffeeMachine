from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 300,  # 300
    "milk": 200,  # 200
    "coffee": 100,  # 100
    "money": 0.0,  # 0.0
}


def report(resources_data):
    """Function will print the actual values for the resources"""
    actual_state = f"""
    Resources - report - actual values:
    Water: {resources_data["water"]}ml
    Milk: {resources_data["milk"]}ml
    Coffee: {resources_data["coffee"]}g
    Money: ${resources_data["money"]}
    """
    return actual_state


def resources_sufficient_check(data, drink):
    """Function will check if the resources are sufficient, step by step,
        if some ingredient is missing, the user will get the information."""
    ingredients_list = ["water", "milk", "coffee"]
    for ingredient in ingredients_list:
        if data[ingredient] < MENU[drink]["ingredients"][ingredient]:
            return f"Sorry there is not enough {ingredient}"
        else:
            return 1


def coffee_price(coffee_drink):
    """Function will prompt the user to input coffee price in coins"""
    price = float(MENU[coffee_drink]["cost"])
    return price


def get_coins():
    """Function will prompt the user to input for each type of coin the
    quantity"""
    quarters = float(input("How many $0.25: "))
    dimes = float(input("How many $0.10: "))
    nickles = float(input("How many $0.05: "))
    pennies = float(input("How many $0.01: "))
    coins = [quarters, dimes, nickles, pennies]
    return coins


def sum_inserted(coins_inserted):
    """Function will calculate the sum based on the list of coins count"""
    client_paid = ((0.25 * coins_inserted[0]) + (0.10 * coins_inserted[1]) +
                   (0.05 * coins_inserted[2]) + (0.01 * coins_inserted[3]))
    return round(client_paid, 2)


def making_coffee():
    """Function will check if the paid amount is enough,
     if not money will be refund, if customer paid more,
      the change will be refund."""
    price = coffee_price(choice)
    print(f"Please insert ${price} in coins.")
    paid = sum_inserted(get_coins())
    if paid < price:
        print("Sorry that's not enough money.\nMoney refunded.")
    else:
        change = round((paid - price), 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        print(f"Enjoy your {choice}.")


def resource_update(data, drink):
    """Function, will update the resources data"""
    resource_items = ["water", "milk", "coffee", "money"]
    drink_items = ["water", "milk", "coffee"]
    coffee_items = []
    data_items = []
    for item in drink_items:
        coffee_items.append(MENU[drink]["ingredients"][item])
    coffee_items.append(MENU[drink]["cost"])
    for item in resource_items:
        data_items.append(data[item])
    resources = []
    resources.append(data_items[0] - coffee_items[0])
    resources.append(data_items[1] - coffee_items[1])
    resources.append(data_items[2] - coffee_items[2])
    resources.append(data_items[3] + coffee_items[3])
    new_resources = {
        "water": resources[0],
        "milk": resources[1],
        "coffee": resources[2],
        "money": resources[3],
    }
    return new_resources


def transaction_processing():
    if resources_sufficient_check(resources, choice) == 1:
        making_coffee()
        return 1
    else:
        print(resources_sufficient_check(resources, choice))


print(logo)
power_on = True  # flag to continue while loop

# Prompt user to make a choice
while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    match choice:
        case "espresso":
            work_in_progress = transaction_processing()
            if work_in_progress == 1:
                resources = resource_update(resources, choice)
        case "latte":
            work_in_progress = transaction_processing()
            if work_in_progress == 1:
                resources = resource_update(resources, choice)
        case "cappuccino":
            work_in_progress = transaction_processing()
            if work_in_progress == 1:
                resources = resource_update(resources, choice)
        case "report":
            print(report(resources_data=resources))
        case "off":
            print("Welcome maintainer, the power is off.")
            power_on = False
