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

COIN = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "pennie": 0.01
}

def report(resources):
    print("Water: ", resources["water"])
    print("Milk: ", resources["milk"])
    print("Coffe: ", resources["coffee"])

coins = [0,0,0,0]
buttonON = True

while buttonON:
    order = input("What would you like? (espresso/latte/cappuccino):")

    if order == "off":
        buttonON = False
    elif order == "report":
        report(resources)
    #elif order == "espresso":
        
        
    