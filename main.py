# 21.9.1
class Trapezium:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def __str__(self):
        return f'Trapezium: {self.a}, {self.b}, {self.h}.'

    def get_area_trapezium(self):
        return 0.5 * (self.a + self.b) * self.h


trap_1 = Trapezium(8, 10, 5)
print(trap_1)
print("Trapezium area: ", trap_1.get_area_trapezium())


# 21.9.2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle :  {self.width}, {self.height}.'

    def get_area(self):
        return self.width * self.height


rect_1 = Rectangle(10, 7)
print(rect_1)
print("Rectangle area:", rect_1.get_area())


# 21.9.3
class Client:
    def __init__(self, name="", surname="", city="", balance=0, currency="руб"):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
        self.currency = currency

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} {self.currency}.'
#21.9.4
    def get_guest(self):
        return f'{self.name} {self.surname}. {self.city}.'


client_1 = Client('Иван', 'Петров', 'Москва', 50)
print(client_1)
print(client_1.get_guest())

guest_1 = Client('Иван', 'Никитин', 'Москва', 20)
guest_2 = Client('Никита', 'Иванов', 'Хабаровск', 540)
guest_3 = Client('Андрей', 'Грибовский', 'Тула', 5000)
guest_4 = Client('Виталий', 'Варенин', 'Уфа', 100)
guest_5 = Client('Александр', 'Пончик', 'Питер', 500)
#21.9.4
guest_list = (guest_1,guest_2,guest_3,guest_4,guest_5)

for guest in guest_list:
    print(guest.get_guest())