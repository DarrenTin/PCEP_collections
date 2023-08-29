class CoffeeMachine:
    def __init__(self, state='on', water=0, milk=0, coffee_beans=0, disposable_cup=0, money=0):
        self.state = state
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cup = disposable_cup
        self.money = money

    def print_instuction(self):
        outputs = "Starting to make a coffee", "Grinding coffee beans", "Boiling water", "Mixing boiled water with crushed coffee beans", "Pouring coffee into the cup", "Pouring some milk into the cup", "Coffee is ready!"
        for item in outputs:
            print(item)

    def cup_to_ingredient(self):
        cups = int(input("Write how many cups of coffee you will need: "))
        print(f"For {cups} cups of coffee you will need: ")
        print(f"{cups * 200} ml of water")
        print(f"{cups * 50} ml of milk")
        print(f"{cups * 15} g of coffee beans")

    def ingredient_to_cup(self):
        water = int(input("Write how many ml of water the coffee machine has: "))
        milk = int(input("Write how many ml of milk the coffee machine has: "))
        coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
        coffee_cups = int(input("Write how many cups of coffe you will need: "))

        water_max = water // 200
        milk_max = milk // 50
        coffee_beans_max = coffee_beans // 15

        max_cup = min(water_max, milk_max, coffee_beans_max)
        if max_cup == coffee_cups:
            print("Yes, I can make that amount of coffee")
        elif max_cup > coffee_cups:
            print(f"Yes, I can make that amount of coffee (and even {max_cup - coffee_cups} more than that)")
        elif max_cup < coffee_cups:
            print(f"No, I can make only {max_cup} cups of coffee")

    def prompt_user(self):
        while self.state == "on":
            user_action = input("Write action (buy, fill, take, remaining, exit): ").lower()
            self.perform_action(user_action)

    def print_report(self):
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cup} disposable cups")
        print(f"${self.money} of money")

    def perform_action(self, action):
        if action == "buy":
            selected_coffee = input("What do you want to buy? 1- espresso, 2-latte, 3-cappuccino, back-to main menu: ) ").lower()
            self.buy_coffee(selected_coffee)
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.print_report()
        elif action == "exit":
            self.state = "off"

    def buy_coffee(self, coffee):
        if coffee == '1':
            self.buy_specific_coffee(250, 0, 16, 4)
        elif coffee == '2':
            self.buy_specific_coffee(350, 75, 20, 7)
        elif coffee == '3':
            self.buy_specific_coffee(200, 100, 12, 6)
        elif coffee == 'back':
            return

    def buy_specific_coffee(self, water_cost, milk_cost, coffee_beans_cost, money_earned):
        if water_cost > self.water:
            print("Sorry, water not enough")
        elif milk_cost > self.milk:
            print("Sorry, milk not enough")
        elif coffee_beans_cost > self.coffee_beans:
            print("Sorry, coffee beans not enough")
        elif self.disposable_cup <= 0:
            print("Sorry, disposable cup not enough")
        else:
            self.water -= water_cost
            self.milk -= milk_cost
            self.coffee_beans -= coffee_beans_cost
            self.disposable_cup -= 1
            self.money += money_earned
            print("I have enough resources, making you a coffee!")

    def fill(self):
        water_filled = int(input("Write how many ml of water you want to add: "))
        milk_filled = int(input("Write how many ml of milk you want to add: "))
        coffee_beans_filled = int(input("Write how many grams of coffee beans you want to add: "))
        disposable_cup_filled = int(input("Write how many disposable cups you want to add: "))
        self.water += water_filled
        self.milk += milk_filled
        self.coffee_beans += coffee_beans_filled
        self.disposable_cup += disposable_cup_filled

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0.0


# cm1 = CoffeeMachine("on", 400, 540, 120, 9, 550.0)