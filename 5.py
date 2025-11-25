import csv

def publishers_list(books_en):
    books_en.seek(0)
    reader = csv.DictReader(books_en, delimiter=';')
    publishers = []

    for book in reader:
        if book['Publisher'] not in publishers:
            publishers.append(book['Publisher'])

    print(
        f'Задание 5:\nКоличество издательств без повторений: {len(publishers)}'
    )
    # print('Издательства:')
    # for i in publishers:
    #     print(i)


if __name__ == '__main__':
    with open('books-en.csv') as books_en:
        publishers_list(books_en)
