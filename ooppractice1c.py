number = input("Acc no:")
name = input("Name:")
balance = float(input("Balance:"))

def balance():
    print(f"Current account balance: {balance}")

def deposit():
    deposit = float(input("Deposit:"))
    balance += deposit
    balance()

def withdraw():
    withdraw = float(input("Withdraw:"))
    balance -= withdraw
    balance()

while True:
    answer = input("<Option>\n1 - balance, 2 - deposit, 3 - withdraw, 4 - exit:")

    if answer == '1':
        balance()
    elif answer == '2':
        deposit()
    elif answer == '3':
        withdraw()
    elif answer == '4':
        break