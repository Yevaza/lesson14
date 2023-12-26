class Car:
    def __init__(self) :
        self.model=""
        self.year=""
        self.manufacturer=""
        self.volume=0.0
        self.color=""
        self.price=""
    def input(self):
        self.model = input("Введите модель автомобиля: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.volume = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def data(self):
        print(f'Модель:, {self.model}')
        print(f'Год выпуска:,{ self.year}')
        print(f'Производитель:, {self.manufacturer}')
        print(f'Объем двигателя:, {self.volume}')
        print(f'Цвет машины:, {self.color}')
        print(f'Цена:, {self.price}')
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_volume(self):
        return self.volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price
car_instance=Car()
car_instance.input()
car_instance.data()

