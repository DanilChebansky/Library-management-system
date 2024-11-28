import json

from src.classes import JsonEditor

# Заводим переменную для вывода списка книг из файла хранения
books = []
with open("books.json", encoding="utf-8") as reading_book:
    for book in json.load(reading_book):
        books.append(book)

# Создаем экземляр класса JsonEditor для работы с библиотекой
json_saver = JsonEditor(books)

# Начинаем цикл программы
while True:

    # Исключаем ошибки ввода команды
    while True:
        print('Если хотите выйти из программы, введите 1')
        user_input = input('Введите действие, которые Вы хотите выполнить: удалить книгу (уд), добавить книгу (до),'
                           ' вывести список книг (сп), найти книгу по id (на) или изменить статус книги (из)\n')
        if not user_input:
            print('Введите букву, определяющую вид команды')
        elif user_input.lower() not in ['уд', 'до', 'сп', 'на', 'из', '1']:
            print('Введите cуществующую команду')
        else:
            break

    # В зависимости от введенной команды выполняем действие с библиотекой или выходим с программы, введя "1"
    if user_input.lower() == 'уд':
        json_saver.book_deliter()
    elif user_input.lower() == 'до':
        json_saver.book_adder()
    elif user_input.lower() == 'сп':
        json_saver.list_book_reader()
    elif user_input.lower() == 'на':
        json_saver.one_book_reader()
    elif user_input.lower() == 'из':
        json_saver.status_editer()
    else:
        break
