resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}

coffee = {
    "espresso": {
        "Water": 50,
        "Coffee": 18
    },
    "latte": {
        "Water": 200,
        "Milk": 150,
        "Coffee": 24
    },
    "cappuccino": {
        "Water": 250,
        "Milk": 100,
        "Coffee": 24
    },
}

def checkResources(resources):
    for i in resources.keys():
        print(i)

checkResources(resources)
    

