class BankAccount:
    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value

    def __str__(self):
        return f'Number = {self.number}\nName = {self.name}\nBalance = {self.balance}'


my_account = BankAccount("001", "Khoo", 2000)
print(my_account)
print(my_account.balance)
my_account.balance = "chaos@$@^^@%"
print(my_account)