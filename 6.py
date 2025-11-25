import csv


def find_most_popular_book(books_file):
    """Find and print the most popular book based on download count."""
    books_file.seek(0)
    reader = csv.DictReader(books_file, delimiter=';')
    books = {}

    for book in reader:
        books[book['Book-Title']] = int(book['Downloads'])

    most_popular_title = max(books, key=lambda k: books[k])
    download_count = books[most_popular_title]
    
    print(
        'Задание 6:\n'
        f'Самая популярная книга: {most_popular_title}\n'
        f'Количество скачиваний: {download_count}'
    )


if __name__ == '__main__':
    with open('books-en.csv', encoding='utf-8') as books_file:
        find_most_popular_book(books_file)
