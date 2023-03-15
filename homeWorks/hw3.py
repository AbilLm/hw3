Abil = 100


class Bank():
    def __init__(self, name, balanse):
        self.name = name
        self.balanse = balanse

    def moneyX(self):
        add = int(input('Введите сумму которую хотите добавить на свой счёт: '))
        self.balanse += add
        print(self.balanse)

    def kill(self):
        return self.balanse == 0

    def __jackpot(self):
        a = self.balanse * 10
        print(a)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Баланс: {self.balanse}'

    def __unite_balanse(self):
        print(self.balanse())
        pass



user = Bank('Abil', 0)
print(user)


