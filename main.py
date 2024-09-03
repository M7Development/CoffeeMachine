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

money = 0


def enoughresources1(water, coffee):
    if water < 0 or coffee < 0:
        # print(str(water) + '\n' + str(coffee))
        if water < 0 and coffee < 0:
            print('Sorry there is not enough water and coffee.')
            return True
        elif water < 0:
            print('Sorry there is not enough water.')
            return True
        elif coffee < 0:
            print('Sorry there is not enough coffee.')
        else:
            print('Some..')
            return True


def enoughresources2(water, milk, coffee):
    if water < 0 or milk < 0 or coffee < 0:
        # print(str(water) + '\n' + str(milk) + '\n' + str(coffee))
        if water < 0 and milk < 0 and coffee < 0:
            print('Sorry there is not enough water, milk and coffee.')
            return True
        elif water < 0 and milk < 0:
            print('Sorry there is not enough water and milk.')
            return True
        elif water < 0 and coffee < 0:
            print('Sorry there is not enough water and coffee.')
            return True
        elif coffee < 0 and milk < 0:
            print('Sorry there is not enough coffee and milk.')
            return True
        elif water < 0:
            print('Sorry there is not enough water.')
            return True
        elif milk < 0:
            print('Sorry there is not enough milk.')
            return True
        elif coffee < 0:
            print('Sorry there is not enough coffee.')
        else:
            print('Some..')
            return True


# TODO 5.Process coins
def insertcoins(userinput):
    paymoney = {
        "q": 0.25,
        "d": 0.1,
        "n": 0.05,
        "p": 0.01
    }
    paid = 0
    print(f"Please insert ${MENU[userinput]['cost']}!")
    while MENU[userinput]['cost'] > paid:
        insertedcoin = input('Please insert now your coins\n').lower()
        if insertedcoin == 'q':
            paid += paymoney['q']
            if MENU[userinput]['cost'] <= paid:
                print(f"Enyoj your {userinput}")
                paid = refundcoins(paid, userinput)
                return round(paid, 2)
            print("You still have to pay $" + str(round(MENU[userinput]['cost'] - paid, 2)))
        elif insertedcoin == 'd':
            paid += paymoney['d']
            if MENU[userinput]['cost'] <= paid:
                print(f"Enyoj your {userinput}")
                paid = refundcoins(paid, userinput)
                return round(paid, 2)
            print("You still have to pay $" + str(round(MENU[userinput]['cost'] - paid, 2)))
        elif insertedcoin == 'n':
            paid += paymoney['n']
            if MENU[userinput]['cost'] <= paid:
                print(f"Enyoj your {userinput}")
                paid = refundcoins(paid, userinput)
                return round(paid, 2)
            print("You still have to pay $" + str(round(MENU[userinput]['cost'] - paid, 2)))
        elif insertedcoin == 'p':
            paid += paymoney['p']
            if MENU[userinput]['cost'] <= paid:
                print(f"Enyoj your {userinput}")
                paid = refundcoins(paid, userinput)
                return round(paid, 2)
            print("You still have to pay $" + str(round(MENU[userinput]['cost'] - paid, 2)))
        else:
            print("This is not any legal coin!")
    refundcoins(paid, userinput)
    return round(paid, 2)


def refundcoins(paid, userinput):
    if paid > MENU[userinput]['cost']:
        refund = round(paid - MENU[userinput]['cost'], 2)
        print(f"Here is ${refund} dollars in change.")
        return paid - refund


# TODO 2.Turning off Coffee Machine
def switchoffmachine(userinput):
    if userinput == 'off':
        print("Coffee machine is switching off!")
        return 'off'


# TODO 3.Print report
def reportprinting(userinput):
    if userinput == 'report':
        print('Water: ' + str(resources['water']) + 'ml\nMilk: ' + str(resources['milk']) + 'ml\nCoffee: ' + str(
            resources['coffee']) + 'g\nMoney: $' + str(money) + '\n')


# TODO 4.Check Resources sufficent?
def checkresources(userinput, resources, money):
    if userinput == 'espresso':
        water = resources['water'] - MENU[userinput]['ingredients']['water']
        coffee = resources['coffee'] - MENU[userinput]['ingredients']['coffee']
        continueservice = enoughresources1(water, coffee)
        if continueservice:
            return resources
        resources['water'] = water
        resources['coffee'] = coffee
        money += insertcoins(userinput)
        return resources, money
    elif userinput == 'latte':
        water = resources['water'] - MENU[userinput]['ingredients']['water']
        milk = resources['milk'] - MENU[userinput]['ingredients']['milk']
        coffee = resources['coffee'] - MENU[userinput]['ingredients']['coffee']
        continueservice = enoughresources2(water, milk, coffee)
        if continueservice:
            return resources
        resources['water'] = water
        resources['milk'] = milk
        resources['coffee'] = coffee
        money += insertcoins(userinput)
        return resources, money
    elif userinput == 'cappuccino':
        water = resources['water'] - MENU[userinput]['ingredients']['water']
        milk = resources['milk'] - MENU[userinput]['ingredients']['milk']
        coffee = resources['coffee'] - MENU[userinput]['ingredients']['coffee']
        continueservice = enoughresources2(water, milk, coffee)
        if continueservice:
            return resources
        resources['water'] = water
        resources['milk'] = milk
        resources['coffee'] = coffee
        money += insertcoins(userinput)
        return resources, money


# TODO 6.Check transaction successful?

# TODO 1.Input of order

inputValue = input("What do you would like? (espresso/latte/cappuccino)\n").lower()

# TODO 7.Make Coffee
# Execution
while 'off' != switchoffmachine(inputValue):
    reportprinting(inputValue)
    if inputValue != 'report':
        resources, money = checkresources(inputValue, resources, money)
        print('Aktueller Stand: ' + str(resources) + ' the machine earned $' + str(money))
    inputValue = input("What do you would like? (espresso/latte/cappuccino)\n").lower()