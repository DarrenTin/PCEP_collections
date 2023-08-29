def print_report():
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cup} disposable cups")
    print(f"${money} of money")

def perform_action(action):
    if action == "buy":
        selected_coffee = input("What do you want to buy? 1- espresso, 2-latte, 3-cappuccino, back-to main menu: ) ").lower()
        buy_coffee(selected_coffee)
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        print_report()
    elif action == "exit":
        global state
        state = "off"

def buy_coffee(coffee):
    if coffee == '1':
        buy_specific_coffee(250, 0, 16, 4)
    elif coffee == '2':
        buy_specific_coffee(350, 75, 20, 7)
    elif coffee == '3':
        buy_specific_coffee(200, 100, 12, 6)
    elif coffee == 'back':
        return

def buy_specific_coffee(water_cost, milk_cost, coffee_beans_cost, money_earned):
    global water, milk, coffee_beans, money, disposable_cup
    if water_cost > water:
        print("Sorry, water not enough")
    elif milk_cost > milk:
        print("Sorry, milk not enough")
    elif coffee_beans_cost > coffee_beans:
        print("Sorry, coffee beans not enough")
    elif disposable_cup <= 0:
        print("Sorry, disposable cup not enough")
    else:
        water -= water_cost
        milk -= milk_cost
        coffee_beans -= coffee_beans_cost
        disposable_cup -= 1
        money += money_earned
        print("I have enough resources, making you a coffee!")

def fill():
    global water, milk, coffee_beans, disposable_cup
    water_filled = int(input("Write how many ml of water you want to add: "))
    milk_filled = int(input("Write how many ml of milk you want to add: "))
    coffee_beans_filled = int(input("Write how many grams of coffee beans you want to add: "))
    disposable_cup_filled = int(input("Write how many disposable cups you want to add: "))
    water += water_filled
    milk += milk_filled
    coffee_beans += coffee_beans_filled
    disposable_cup += disposable_cup_filled

def take():
    global money
    print(f"I gave you ${money}")
    money = 0.0

state = "on"
water, milk, coffee_beans, disposable_cup, money = 400, 540, 120, 9, 550.0

while state == "on":
    # print_report()
    user_action = input("Write action (buy, fill, take, remaining, exit): ").lower()
    perform_action(user_action)