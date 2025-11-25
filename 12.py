import csv


def count_long_titles(books):
    """Count records with titles longer than 30 characters."""
    books.seek(0)
    reader = csv.DictReader(books, delimiter=';')
    counter = 0
    for row in reader:
        if len(str(row['Название'])) > 30:
            counter += 1
    print(
        'Задание 1:\n'
        f'Количество записей, у которых название длиннее 30 символов: {counter}'
    )


def find_books_by_author(books):
    """Find books by author published in specific years."""
    books.seek(0)
    reader = csv.DictReader(books, delimiter=';')
    print('Задание 2:')
    author = input('Введите ФИО автора: ')
    found_books = []
    
    for row in reader:
        if author == row['Автор (ФИО)']:
            year = int(row['Дата поступления'][6:10])
            if year in [2014, 2016, 2017]:
                found_books.append(row['Название'])
    
    if found_books:
        print('Найденные книги:')
        for book in found_books:
            print(book)
    else:
        print('Книги не были найдены')


if __name__ == '__main__':
    with open('books.csv', encoding='utf-8') as books:
        count_long_titles(books)
        find_books_by_author(books)
