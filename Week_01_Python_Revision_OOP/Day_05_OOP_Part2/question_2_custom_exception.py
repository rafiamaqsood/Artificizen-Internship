#  Define a custom exception InsufficientBalanceError and raise it inside the BankAccount class from Day 4. 

class InsufficientBalanceError (Exception):
    pass


class BankAccount:
    def __init__(self , balance):
        self.balance= balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        else:      
            print(f"Total balance is {self.balance}")
            self.balance += amount
            print(f"Rs {amount} is deposited")
            print(f"After deposit Total balance is {self.balance}")

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Withdrawl amount must be positive.")
        elif amount>self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        else:
         print(f"Total balance is {self.balance}")
         self.balance -= amount
         print(f"Rs {amount} is withdrawn")
         print(f"After withdrawal Total balance is {self.balance}")

account= BankAccount(5000)
account.deposit(1000)
try:
    account.withdraw(7000)
except InsufficientBalanceError as e:
    print(e)
print("total balance is", account.balance)