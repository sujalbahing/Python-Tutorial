# class Animal:
    
#     def __init__(self, name):
#         print("Constructor invoked")
#         self.name = name
    
#     def eat(self):
#         print(self.name)
#         print("I can eat")
    
#     def sleep(self):
#         print("I can sleep")
        
# class Dog(Animal):
    
#     def bark(self):
#         print("Woof")
    
# dog1 = Dog('German Shepherd')
# print(dog1.name)

# dog1.eat()

# dog1.sleep()
     
     
    # _ = private
    # __ = protected
        
# class BankAccount:
#     def __init__(self,account_number,balance):
#         self._account_number = account_number
#         self._balance = balance
        
#     def _deposit(self,amount):
        
#         self._balance += amount
#         print(f"Deposit successful. New Balance: ${self._balance}")
        
#     def check_balance(self):
#         print(f"Your current balance is: ${self._balance}")
        
#     def withdraw(self, amount):
#         self._balance -= amount
#         print(f"Withdrawal successful. New Balance: ${self._balance}")
        
# account = BankAccount('1234',1000)
# account._deposit(-100)
# account.withdraw(1500)
# account.check_balance()

# print(account._account_number)


class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number
        self._balance = balance
    
    def __deposit(self,amount):
        self._balance += amount
        print(f"Deposit successful. New Balance : ${self._balance}")

    def check_balance(self):
        print(f"Current Balance : {self._balance}")
    
    def withdraw(self,amount):
        self._balance -= amount
        print(f"Wdithdraw successful. New Balance : ${self._balance}")

    
account = BankAccount('1234',1000)
# account.deposit(-100)
# account.withdraw(1500)
# account.check_balance()

print(account._account_number)