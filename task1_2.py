class Book:
    def __init__(self):
        self.name=""
        self.year=""
        self.publisher=""
        self.genre=''
        self.author=""
        self.price=""
    def input(self):
        self.name = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = (input("Введите жанр: "))
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def data(self):
        print(f'Название книги:, {self.name}')
        print(f'Год выпуска:,{ self.year}')
        print(f'Издатель:, {self.publisher}')
        print(f'Жанр:, {self.genre}')
        print(f'Автор:, {self.author}')
        print(f'Цена:, {self.price}')
    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price
book_instance=Book()
book_instance.input()
book_instance.data()
