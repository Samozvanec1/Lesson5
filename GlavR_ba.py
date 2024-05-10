class Warrior():

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep (self):
        print(f"{self.name} лёг спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьёт врагов")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f" имя воина - {self.name} ")
        print(f" цвет волос воина - {self.hair_color} ")
        print(f" сила воина - {self.power} ")
        print(f" выносливость воина - {self.endurance} ")


woin1 = Warrior("Александр", 50, 100, "Рыжий")
#woin2 = Warrior("Вародин", 11, 5, "Рыжий")



#print(woin2.endurance)
#woin2.sleep()
#print(woin2.endurance)
#print(woin2.power)
#woin2.eat()
#print(woin2.power)

woin1.sleep()
woin1.eat()
woin1.hit()
woin1.walk()
woin1.info()


woin2.sleep()
woin2.eat()
woin2.hit()
woin2.walk()
woin2.info()


#for i in range(100):
#    my_warriors.append(Warrior("Александр", 100, 100, "Рыжий"))
#for i in my_warriors:
#    i.info()