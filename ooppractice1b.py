number = input("Acc no:")
name = input("Name:")
balance = float(input("Balance:"))

while True:
    answer = input("<Option> 1 - balance, 2 - deposit, 3 - withdraw, 4 - exit:")
    if answer == '1':
        print(f"Current account balance: {balance}")
    elif answer == '2':
        deposit = float(input("Deposit:"))
        balance  += deposit
        print(f"Current account balance: {balance}")
    elif answer == '3':
        withdraw = float(input("Withdraw:"))
        balance -= withdraw
        print(f"Current account balance: {balance}")
    elif answer == '4':
        break