class Stadium :
    def __init__(self):
        self.name=""
        self.year=""
        self.country =""
        self.city=''
        self.capacity=""
    
    def input(self):
        self.name = input("Введите название стадиона: ")
        self.year = int(input("Введите дату открытия : "))
        self.country = input("Введите страну: ")
        self.city = (input("Введите город: "))
        self.capacity = int(input("Введите вместимость: "))
    

    def data(self):
        print(f'Название стадиона:, {self.name}')
        print(f'Дата открытия:,{ self.year}')
        print(f'Страна:, {self.country }')
        print(f'Город:, {self.city}')
        print(f'Вместимость:,{self.capacity}')
    
    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_country(self):
        return self.country 

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity
stadium_instance=Stadium()
stadium_instance.input()
stadium_instance.data()