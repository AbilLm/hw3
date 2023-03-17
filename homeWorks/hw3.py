Abil = 100
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        add = int(input('Введите сумму которую хотите добавить на свой счёт: '))
        self._balance += add
        print(self._balance)

    def kill(self):
        return self._balance == 0

    def _jackpot(self):
        a = self._balance * 10
        print(a)

    def __str__(self):
        return f'Имя: {self._name}\n' \
               f'Баланс: {self._balance}'

    def _unite_balance(self):
        print(self._balance)
        pass

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance


class NewBank(Bank):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance


user = NewBank('Abil', 0)
print(user)

user.set_name('Бека')
print(user.get_name())

user.name = 'Жаннат'
print(user.name)

user.set_balance(100)
print(user.get_balance())

user.balance = 200
print(user.balance)


