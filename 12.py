import csv


def row_len(books):
    books.seek(0)
    reader = csv.DictReader(books, delimiter=';')
    counter = 0
    for row in reader:
        if len(str(row['Название'])) > 30:
            counter += 1
    print(f'Задание 1:\nКоличество записей, у которых название длиннее 30 символов: {counter}')


def find_author(books):
    books.seek(0)
    reader = csv.DictReader(books, delimiter=';')
    print('Задание 2:')
    author = input('Введите ФИО автора: ')
    found_books = []
    for row in reader:
        if author == row['Автор (ФИО)']:
            if int(row['Дата поступления'][6:10]) in [2014, 2016, 2017]:
                found_books.append(row['Название'])
    if len(found_books) != 0:
        print('Найденные книги:')
        for book in found_books:
            print(book)
    else:
        print('Книги не были найдены')


if __name__ == '__main__':
    with open('books.csv') as books:
        row_len(books)
        find_author(books)
