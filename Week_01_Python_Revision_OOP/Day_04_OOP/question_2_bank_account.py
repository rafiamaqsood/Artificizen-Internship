# Create a BankAccount class with deposit() and withdraw() methods; prevent withdrawals beyond the balance. 

class BankAccount:
    def __init__(self , balance):
        self.balance= balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:      
            print(f"Total balance is {self.balance}")
            self.balance += amount
            print(f"Rs {amount} is deposited")
            print(f"After deposit Total balance is {self.balance}")

    def withdraw(self, amount):
        if amount <=0:
            print("Withdrawl amount must be positive.")
        elif amount>self.balance:
            print("Insufficient balance")
        else:
         print(f"Total balance is {self.balance}")
         self.balance -= amount
         print(f"Rs {amount} is withdrawn")
         print(f"After withdrawal Total balance is {self.balance}")

account= BankAccount(5000)
account.deposit(1000)
account.withdraw(7000)
print("total balance is", account.balance)