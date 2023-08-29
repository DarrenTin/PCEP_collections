# design is a subjective matter
# tuples are more memory efficient

# make deep dict
# ask what would you like (expresso/latte/cappuccino)
# hidden: off, report
# ask dimes
# ask nickles
# ask pennies inserted
# reduce water/milk/coffee after making coffee

# first step: decompose component, def function with 'pass


def print_report():
        print(f"Water: {water} ml")
        print(f"Milk: {milk} ml")
        print(f"Coffee: {coffee} g")
        print(f"Money: ${money}")

def prompt_user():
    pass

def make_drink(drink):
    if drink == "espresso":
        validate_drink(200, 30, 36, 2.5)
    elif drink == "latte":
        validate_drink(180, 20, 48, 3.5)
    elif drink == "cappuccino":
        validate_drink(175, 25, 55, 4.5)
    else:
        print("Sorry, your drink is not exist")
        return
    
    
def validate_drink(water_required, milk_required, coffee_required, price):
    global water, milk, coffee, money
    if water_required > water:
        print("Sorry there is not enough water")
        return
    if milk_required > milk:
        print("Sorry there is not enough milk")
        return
    if coffee_required > coffee:
        print("Sorry there is not enough coffee")
        return
    coin = insert_coin()
    if coin < price:
        print("Sorry, that's not enough money. Money refunded.")
        return
    elif coin > price:
        print(f"Here is ${coin - price:.2f} in charge.")
        water -= water_required
        milk -= milk_required
        coffee -= coffee_required
        money += price
        print("Here is your latte. Enjoy!")

def insert_coin():
    print("\n\n____Insert coin____")
    quarters = int(input("Quarters:"))
    dimes = int(input("Dimes:"))
    nickles = int(input("Nickles:"))
    pennies = int(input("Pennies:"))
    monetary_value = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    # monetary_value = round(monetary_value, 2)
    # print(f"Value = ${monetary_value:.2f}")
    return monetary_value

coffee_status = 'on'
water, milk, coffee, money = 1000, 100, 200, 0.0
while coffee_status == 'on':
    user_input = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_input == 'off':
        coffee_status = 'off'
    elif user_input == 'report':
        print_report()
    else:
        make_drink(user_input)