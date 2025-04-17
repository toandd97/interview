class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Thuộc tính private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def get_balance(self):  # Getter
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())  # 1000
account.deposit(500)
print(account.get_balance())  # 1500