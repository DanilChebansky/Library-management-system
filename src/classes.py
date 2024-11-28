import json


class Book:
    """Класс для работы с книгами"""

    def __init__(self, title: str, author: str, year: int):
        books = []
        with open("books.json", encoding="utf-8") as reading_book:
            for book in json.load(reading_book):
                books.append(book)
        self.id = sorted(books, key=lambda x: x['id'])[-1]['id'] + 1 if len(books) != 0 else 1
        self.title = title
        self.author = author
        self.year = int(year)
        self.status = "в наличии"

    def __dict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }


class JsonEditor:
    """Класс для сохранения книг в JSON-файл"""

    def __init__(self, books: list = None):
        with open("books.json", "w", encoding="utf-8") as editing_file:
            json.dump(books, editing_file, indent=4, ensure_ascii=False)

    def book_adder(self):
        """Добавляет книгу в JSON-файл"""
        while True:
            title = input('Введите название книги\n')
            author = input('Введите автора книги\n')
            year = input('Введите год издания книги\n')
            if not title or not author or not year:
                print('Введите все данные для книги')
            elif not year.isdigit():
                print('Введите год цифрами')
            elif int(year) > 2024:
                print('Год не может быть больше текущего')
            else:
                break
        # Создаем экземпляр класса Book
        new_book = Book(title, author, int(year))
        # Добавляем в список все книги из json-файла и новую книгу
        new_books_list = []
        with open("books.json", "r+", encoding="utf-8") as appending_book:
            for book in json.load(appending_book):
                new_books_list.append(book)
            new_books_list.append(new_book.__dict__())
            print(f'Книга {new_book.title} добавлена')
        # Записываем список в json-файл
        with open("books.json", "w", encoding="utf-8") as appending_book:
            appending_book.write(json.dumps(sorted(new_books_list, key=lambda x: x['id']), indent=4,
                                            ensure_ascii=False))

    def list_book_reader(self):
        """Выводит все книги из JSON-файла"""
        with open("books.json", encoding="utf-8-sig") as reading_book:
            lst = []
            for book in json.load(reading_book):
                lst.append(book)
                print(book)
            return lst

    def one_book_reader(self):
        """Выводит одну книгу из JSON-файла"""
        while True:
            book_id = input('Введите id книги, которую хотите найти\n')
            if not book_id or not book_id.isdigit():
                print('Введите id в числовом формате')
            else:
                break
        with open("books.json", encoding="utf-8") as reading_book:
            checker = 0
            for book in json.load(reading_book):
                if int(book_id) == book['id']:
                    checker += 1
                    print(book)
                    return book
                if checker != 0:
                    print('Такая книга не найдена')
                    return 'Такая книга не найдена'

    def book_deliter(self):
        """Удаляет выбранную книгу в JSON-файле"""
        while True:
            new_books_list = []
            book_id = input('Введите id книги, которую хотите найти\n')
            if not book_id or not book_id.isdigit():
                print('Введите id в числовом формате')
            else:
                break
        # Ищем книгу по id и игнорируем её при добавлении книг в список
        with open("books.json", "r+", encoding="utf-8") as deliting_book:
            checker = 0
            for book in json.load(deliting_book):
                if int(book_id) == book["id"]:
                    checker += 1
                    print(f'Книга {book["title"]} удалена')
                    continue
                else:
                    new_books_list.append(book)
            if checker == 0:
                print('Книги с таким id не найдено')
        # Записываем список в json-файл
        with open("books.json", "w", encoding="utf-8") as appending_book:
            appending_book.write(json.dumps(sorted(new_books_list, key=lambda x: x['id']), indent=4,
                                            ensure_ascii=False))

    def status_editer(self):
        """Меняет статус выбранной книги в JSON-файле"""
        while True:
            new_books_list = []
            book_id = input('Введите id книги, у которой меняется статус\n')
            if not book_id or not book_id.isdigit():
                print('Введите id в числовом формате')
            else:
                break
        # Ищем книгу по id, меняем её статус на один из двух вариантов, и добавляем книгу в список, остальные оставляем
        # неизменными
        with open("books.json", "r+", encoding="utf-8") as editing_book:
            checker = 0
            for book in json.load(editing_book):
                if int(book_id) == book["id"]:
                    checker += 1
                    if book['status'] == 'в наличии':
                        book['status'] = 'выдана'
                    else:
                        book['status'] = 'в наличии'
                    print(f'Статус книги {book["title"]} изменен ({book['status']})')
                new_books_list.append(book)
            if checker == 0:
                print('Книги с таким id не найдено')
        # Записываем список в json-файл
        with open("books.json", "w", encoding="utf-8") as appending_book:
            appending_book.write(json.dumps(sorted(new_books_list, key=lambda x: x['id']), indent=4,
                                            ensure_ascii=False))
