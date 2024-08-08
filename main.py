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
    "money": 0.0,
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


power_on = True  # flag to continue while loop

# Prompt user to make a choice
while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    match choice:
        case "espresso":
            print("Espresso")
        case "latte":
            print("Latte")
        case "cappuccino":
            print("Cappuccino")
        case "report":
            print(report(resources_data=resources))
        case "off":
            print("Welcome maintainer, the power is off.")
            power_on = False
