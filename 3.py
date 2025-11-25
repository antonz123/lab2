import random
import csv


def extract_year(date_string):
    """Extract year from date string in format DD.MM.YYYY."""
    date_parts = date_string.split('.')
    year_part = date_parts[2]
    
    # Remove extra spaces
    while '  ' in year_part:
        year_part = year_part.replace('  ', ' ')
    
    year_components = year_part.split(' ')
    if year_components[0] != ' ':
        return year_components[0]
    else:
        return year_components[1]


def generate_book_list(books_file):
    """Generate a list of 20 random books with formatted information."""
    twenty_books = []
    
    for i in range(20):
        books_file.seek(0)
        reader = csv.DictReader(books_file, delimiter=';')

        # Skip random number of rows
        for _ in range(random.randint(1, 300)):
            fields = next(reader)
        
        date = extract_year(fields["Дата поступления"])
        author = fields['Автор (ФИО)']
        name = fields['Название']
        
        # Format book entry based on available data
        if not date and not author:
            book_entry = (
                f"{i + 1}. Автор неизвестен. {name} - "
                "дата поступления неизвестна."
            )
        elif not date:
            book_entry = f"{i + 1}. {author}. {name} - дата поступления неизвестна."
        elif not author:
            book_entry = f"{i + 1}. Автор неизвестен. {name} - {date}."
        else:
            book_entry = f"{i + 1}. {author}. {name} - {date}."
        
        twenty_books.append([book_entry])
    
    return twenty_books


if __name__ == '__main__':
    with open('books.csv', encoding='utf-8') as books_file, \
         open('twenty_books.csv', 'w', newline='', encoding='utf-8') as output_file:
        
        writer = csv.writer(
            output_file, 
            delimiter=';', 
            quoting=csv.QUOTE_NONE, 
            escapechar='\\'
        )
        writer.writerows(generate_book_list(books_file))
