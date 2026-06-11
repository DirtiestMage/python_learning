class bankAccount:
    def __init__(account, name,balance):
        account.name = name
        account.balance = balance
    def deposit(account, amount):
        account.balance += amount
    def withdraw(account, amount):
        account.balance -= amount
    def __str__(account):
        return (f'Account Holder: {account.name}, Balance: {account.balance}')
    def __int__(account):
        return account.balance


myaccount = bankAccount('Aditya', 1000)

myaccount.deposit(500)
print(myaccount.balance)
print(myaccount)