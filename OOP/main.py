from bank import BankAccount

b1 = BankAccount("56789", "Felicity", 500.0)
b2 = BankAccount("12345", "Vivian", 190.0)

b1.withdraw(100.0)
b2.deposit(50.0)


print(b1.balance)
print(b2.balance)

print(b1)
print(b2)

print(b1 > b2)
