from bank_account import *
Baba = BankAccount(1000, "Babawale")
Quad = BankAccount(2000, "Quadri")
Baba.get_balance()
Quad.get_balance()

Baba.deposit(2000)
Baba.Withdraw(20000)
Baba.Withdraw(10)

Baba.Transfer(5000, Quad)
Baba.Transfer(500, Quad)
Quad.Transfer(500, Baba)

Yomi = InterestAccout(1000, "Yomi")
Yomi.get_balance()
Yomi.deposit(200)
Yomi.Transfer(100, Baba)
Yomi.get_balance()

Yemi = Savings_account(1000, "Yemi")
Yemi.get_balance()
Yemi.deposit(200)
Yemi.Transfer(1000, Quad)
Yemi.Transfer(10000, Quad)
Yemi.get_balance()

