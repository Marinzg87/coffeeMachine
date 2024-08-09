from art import logo

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
    "water": 300, # 300
    "milk": 200, # 200
    "coffee": 100, # 100
    "money": 0.0, # 0.0
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


def resources_sufficient(resources_data, coffee_type):
    """"Function will check if the resources are sufficient, step by step,
    if some ingredient is missing, the user will get the information."""
    resource_water = resources_data["water"]
    resource_milk = resources_data["milk"]
    resource_coffee = resources_data["coffee"]
    coffee = MENU[coffee_type]
    ingredients = coffee["ingredients"]
    coffee_water = ingredients["water"]
    try:
        coffee_milk = ingredients["milk"]
    except KeyError:
        coffee_milk = 0
    coffee_coffee = ingredients["coffee"]
    if resource_water < coffee_water:
        return "Sorry there is not enough water."
    elif resource_milk < coffee_milk:
        return "Sorry there is not enough milk."
    elif resource_coffee < coffee_coffee:
        return "Sorry there is not enough coffee."
    else:
        return "resources_ok"


def coffee_price(coffee_type):
    """Function will prompt the user to input coffee price in coins"""
    price = MENU[coffee_type]["cost"]
    return price


def get_coins():
    """Function will prompt the user to input for each type of coin the
    quantity"""
    quarters = float(input ("How many $0.25: "))
    dimes = float(input ("How many $0.10: "))
    nickles = float(input ("How many $0.05: "))
    pennies = float(input ("How many $0.01: "))
    coins = [quarters, dimes, nickles, pennies]
    return coins


def sum_inserted(coins_inserted):
    """Function will calculate the sum based on the list of coins count"""
    paid = ((0.25 * coins_inserted[0]) + (0.10 * coins_inserted[1]) +
            (0.05 * coins_inserted[2]) + (0.01 * coins_inserted[3]))
    return round(paid, 2)


def resources_update(resources_data, coffee_type):
    """Function will update the resources after making the coffee"""
    resource_water = resources_data["water"]
    resource_milk = resources_data["milk"]
    resource_coffee = resources_data["coffee"]
    resource_money = resources_data["money"]
    coffee = MENU[coffee_type]
    ingredients = coffee["ingredients"]
    coffee_water = ingredients["water"]
    try:
        coffee_milk = ingredients["milk"]
    except KeyError:
        coffee_milk = 0
    coffee_coffee = ingredients["coffee"]
    coffee_money = coffee["cost"]
    resource_water -= coffee_water
    resource_milk -= coffee_milk
    resource_coffee -= coffee_coffee
    resource_money += coffee_money
    resources = {
    "water": resource_water,
    "milk": resource_milk,
    "coffee": resource_coffee,
    "money": resource_money,
    }
    return resources


def make_coffee(resources, choice):
    """Function will check the resources, process coins, validate the
    transaction, prepare the drink"""
    resource_check = resources_sufficient(resources, choice)
    if not resource_check == "resources_ok":
        print(resources_sufficient(resources, choice))
    else:
        price = coffee_price(choice)
        print(f"Please insert ${price} in coins.")
        inserted = sum_inserted(get_coins())
        if inserted < price:
            print("Sorry that's not enough money.\nMoney refunded.")
        else:
            change = round((inserted - price), 2)
            if change > 0:
                print(f"Here is ${change} dollars in change.")
            new_resources = resources_update(resources, choice)
            resources.clear()
            resources = new_resources
            print(f"Enjoy your {choice}.")
            return resources


print(logo)
power_on = True  # flag to continue while loop

# Prompt user to make a choice
while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    match choice:
        case "espresso":
            resources = make_coffee(resources, choice)
        case "latte":
            resources = make_coffee(resources, choice)
        case "cappuccino":
            resources = make_coffee(resources, choice)
        case "report":
            print(report(resources_data=resources))
        case "off":
            print("Welcome maintainer, the power is off.")
            power_on = False
