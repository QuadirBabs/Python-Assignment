class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initailAmount, AccountName):
        self.balance = initailAmount
        self.name = AccountName
        print(f"\n Account '{self.name}' created. \n Balance = ${self.balance:.2f}")
    
    def get_balance(self):
          print(f"\n Account '{self.name}' Balance = ${self.balance:.2f}")
          
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposite complete")
        
        self.get_balance()
        
    def ViableTranaction (self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n Sorry, insufficient Balance! Account '{self.name}' only has a balance of ${self.balance:.2f}")
            
    def Withdraw(self, amount):
        try:
            self.ViableTranaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw Succecful!")
            self.get_balance()
        except BalanceException as error:
            print(f"\n Withdrawal interupted!:{error}")
    
    def Transfer(self, amount, account):
        try:
            print("**********\n\n Beginning  Transfer...🚀")
            self.ViableTranaction(amount)
            self.Withdraw(amount)
            account.deposit(amount)
            print("\n Transfer Completed!\n\n **********✅")
            self.get_balance()
        except BalanceException as error:
            print(f"\n Transfer interupted.❌:{error}")
            
class InterestAccout(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposite Completed.✔")
        self.get_balance()
class Savings_account(InterestAccout):
    def __init__(self, initailAmount, AccountName):
        super().__init__(initailAmount, AccountName)
        self.fee = 5
    
    def Withdraw(self, amount):
        try:
            self.ViableTranaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw Succecful!")
            self.get_balance()
        except BalanceException as error:
            print(f"\n Withdrawal interupted!:{error}")
        
        