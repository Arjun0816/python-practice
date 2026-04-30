class Bank:
    def __init__(self):
        self._balance = 1000
    def show_balance(self):
        print("Balance:",self._balance)
    def deposit(self,amount):
        self._balance += amount
        print("deposited:",amount)
b1 = Bank()
b1.show_balance()
b1.deposit(1000)
b1.show_balance()
