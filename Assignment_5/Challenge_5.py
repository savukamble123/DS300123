class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate*self.balance)/100



demo1 = SavingsAccount("Ashish", 2000, 5) 
demo1.withdrawal(500)
print(demo1.getBalance())
demo1.deposit(500)
print(demo1.getBalance())
print(demo1.interestAmount())