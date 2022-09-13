class BankAccount:
    def __init__(self, balance, income):
        self.__balance = balance
        self.__income = income

    @property
    def balance(self):
        return self.__balance

    @property
    def income(self):
        return self.__income

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @income.setter
    def income(self, value):
        self.__income = value

    def __str__(self):
        return f'{self.__income}  {self.balance}'


acc1 = BankAccount(19000, 10000)
acc2 = BankAccount(233000, 1000)

print(acc1)
print(acc2)
