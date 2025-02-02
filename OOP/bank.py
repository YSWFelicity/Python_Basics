class BankAccount:

    # Constructor
    def __init__(self, accountNumber, accountName, balance):

        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def __str__(self):
        return "({}, {})".format(self.accountName, self.balance)
        return "(" + self.accountName + ", " + str(self.balance) + ")"

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance < other.balance
