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