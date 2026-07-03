# Write a class with a private attribute, exposing it safely through @property.

class BankAccount:

    def __init__(self , account_password):
        self.__acc_password= account_password
    @property
    def acc_password(self):
        return self.__acc_password

account= BankAccount("rafia123")
print(account.acc_password)