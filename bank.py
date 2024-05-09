#  определить класс Account? имитирующий банковский счет
# Класс должен включать атрибуты для хранения идентификаторов владельца, баланс счета
# и методы для депозита (пополнения) и снтия средств, усли на счету достаточно средств
class Account ():

    def __init__(self, id, balance = 0 ):
        self.id = id
        self.balance = balance

    def dipozit (self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счётю  Сумма на счету - {self.balance}")

    def withdraw (self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счету")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли  {money}  рублей. Остаток на счёте:  {self.balance}")

    def all_balance (self):
        print(f"телущий баланс - {self.balance}")



man = Account( 3465868, 449)


man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.dipozit(23000)