# clean code - performance, maintanability
# most simple version

answer = "y"

number = input("Acc no:")
name = input("Name:")
balance = float(input("Balance:"))

while answer == "y":
    withdraw = float(input("Withdraw:"))
    balance -= withdraw
    print(f"Current account balance: {balance}")

    deposit = float(input("Deposit:"))
    balance  += deposit
    print(f"Current account balance: {balance}")

    answer = input("Continue (y/n):")