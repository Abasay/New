from menu import MENU as coffee_menu

order = input("What would you like? (espresso/latte/cappuccino): ")

water = 300
milk = 200
coffee = 100
money = 0

def report():
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

report()


if order == "espresso":
    water -= coffee_menu["espresso"]["ingredients"]["water"]
    milk = 0
    coffee -= coffee_menu["espresso"]["ingredients"]["coffee"]
    money = coffee_menu["espresso"]["cost"]
elif order == "latte":
    water -= coffee_menu["latte"]["ingredients"]["water"]
    milk -= coffee_menu["latte"]["ingredients"]["milk"]
    coffee -= coffee_menu["latte"]["ingredients"]["coffee"]
    money = coffee_menu["latte"]["cost"]
    print(money)

elif order == "cappuccino":
    water -= coffee_menu["cappuccino"]["ingredients"]["water"]
    milk -= coffee_menu["cappuccino"]["ingredients"]["milk"]
    coffee -= coffee_menu["cappuccino"]["ingredients"]["coffee"]
    money = coffee_menu["cappuccino"]["cost"]


def recipes_check():
    if water < 0:
        print("Ooops, there is no enough water.")
    elif milk < 0:
        print("Ooops, there is no enough milk.")
    elif coffee < 0:
        print("Ooops, there is no enough coffee.")


penny, dime, nickel, quarter = 0.01, 0.10, 0.05, 0.25


def money_input():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    quarters = quarters * quarter
    dimes = dimes * dime
    nickels = nickels * nickel
    pennies = pennies * penny

    print(quarters, dimes, nickels, pennies)
    sum = quarter + dimes + nickels + pennies
    print(sum)

    return sum

money_input_amount = money_input()

print(money_input_amount)
if money_input_amount > money:
    print(f"Here is your coffee. Here is the change {round((money_input_amount - money), 2)}")
elif money_input_amount < money:
    print(f"Here is your coffee.")
