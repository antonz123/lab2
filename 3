import random
import csv


def get_year(new_date):
    new_date = new_date.split('.')
    year = new_date[2]
    while '  ' in year:
        year = year.replace('  ', ' ')
    year = year.split(' ')
    if year[0] != ' ':
        return year[0]
    else:
        return year[1]
def read_line(Books):
    twenty_books = []
    for i in range(20):
        Books.seek(0)
        reader = csv.DictReader(Books, delimiter=';')

        for row in range(random.randint(1, 300)):
            fields = next(reader)
        date = get_year(fields["Дата поступления"])
        author = fields['Автор (ФИО)']
        name = fields['Название']
        if len(date) == 0:
            twenty_books.append([f"{i + 1}. {author}. {name} - дата поступления неизвестна."])
        elif len(author) == 0:
            twenty_books.append([f"{i + 1}. Автор неизвестен. {name} - {date}."])
        elif len(date) == 0 and len(author) == 0:
            twenty_books.append([f"{i + 1}. Автор неизвестен. {name} - дата поступления неизвестна."])
        else:
            twenty_books.append([f"{i + 1}. {author}. {name} - {date}."])
    return twenty_books


if __name__ == '__main__':
    with open('books.csv') as Books, open('twenty_books.csv', 'w', newline='', encoding='utf-8') as Twenty_books:
        writer = csv.writer(
            Twenty_books, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\'
        )
        writer.writerows(read_line(Books))
