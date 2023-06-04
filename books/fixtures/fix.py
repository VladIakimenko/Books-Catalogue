# This script converts dumps from the original 'so-books.ru' project to the one required by this project version

import json

if __name__ == '__main__':
    with open('data.json', 'rt', encoding='UTF-8') as filehandle:
        data = json.load(filehandle)

    result = []
    for book in data:
        if book['model'] == 'books.books':
            book['fields']['pub_year'] = book['fields'].pop('year')
            book['model'] = 'books.book'
            book['fields'].pop('box')
            book['fields']['publisher'] = book['fields'].pop('made_in')
            book['fields']['name'] = book['fields']['name'].rstrip('.')
            result.append(book)

    with open ('books.json', 'wt', encoding='UTF-8') as filehandle:
        json.dump(result, filehandle, indent=4)

