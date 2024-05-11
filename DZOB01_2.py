class Store():

    def __init__(self, name, adress):
        self.naz = name
        self.adress = adress
        self.items = {}

    def new_item (self, item_naz, item_price):
        self.items[item_naz] = item_price


    def delete_item (self, item_naz):
        if item_naz in self.items:
            del self.items[item_naz]

    def take_price (self, item_naz):
        return self.items.get(item_naz, None)




    def obnovi_price (self, item_naz, new_price):
        if item_naz in self.items:
            self.items[item_naz] = new_price

    def vse_berem (self):
        for i in self.items:
            print(i, self.items[i])


gum = Store ( "Гум", "Красная площадь д3")
cum = Store ("Цум", "Петровка д2")
elis = Store ("Елисеевский гастроном", "Тверская д14")


print(" У кремля ", gum.adress)



gum.new_item("Бананы", 170)
gum.new_item("Помидоры", 290)
gum.new_item("Яйца", 28)

cum.new_item("Бананы", 150)
cum.new_item("Уши Осла", 720)
cum.new_item("Дуриан", 1200)
cum.new_item("Яйца", 28)

elis.new_item("Нос Волондеморта", 159732)
elis.new_item("Бёдра бобра", 720)
elis.new_item("Дуриан", 1150)
elis.new_item("Яйца", 28)

gum.vse_berem()

print(f"В магазине {gum.naz} по адресу {gum.adress} бананы стоят {gum.take_price ('Бананы')}")

gum.delete_item("Помидоры")

gum.new_item("Нос Волондеморта", 159732)

gum.obnovi_price("Нос Волондеморта", 10000000)



print("После всех махинаций список товаров обновился:")
gum.vse_berem()

print("Уценка носов:")


print(gum.take_price("Нос Волондеморта"))

gum.obnovi_price("Нос Волондеморта", 1099999)

gum.vse_berem()