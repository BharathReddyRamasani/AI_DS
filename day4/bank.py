class Bank:
    def __init__(self, balance=0):
        self.__balance = balance  # private variable
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}, New balance: Rs.{self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrawl Rs.{amount}, New balance: Rs.{self.__balance}")
    def get_balance(self):
        return self.__balance
b = Bank(500)
b.deposit(200) 
b.withdraw(100) 
print("Current Balance:", b.get_balance())
