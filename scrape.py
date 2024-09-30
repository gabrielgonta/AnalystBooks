from category import *
from app import *
from book import *

import requests
from logs import LOGGER

def test_category():

    session = requests.Session()
    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3'

    cat_loader = CategoryLoader(session, url)
    cat = cat_loader.load()

    print(repr(cat))
    print(cat)

    if cat is not None:
        cat_exporter = CategoryExporter(cat)
        cat_exporter.to_csv('csv/' + cat.category_name + '.csv')

def test_book():
    session = requests.Session()
    url = 'http://books.toscrape.com/catalogue/the-third-wave-an-entrepreneurs-vision-of-the-future_862/index.html'
    book_loader = BookLoader(url, session)
    a_book = book_loader.load()
    a_book.add_version()
    print(repr(a_book))
    book_exporter = BookExporter(a_book)
    file_name = 'csv/a_book.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        book_exporter.to_csv(f)

    print(a_book)

    # book_exporter.export_img('img')


def main():
    args = ArgParser()
    the_parameters = args.read_parameters()
    my_app = BooksToScrape(the_parameters)
    my_app.scrapping()
    print(my_app)

if __name__ == '__main__':
    main()
