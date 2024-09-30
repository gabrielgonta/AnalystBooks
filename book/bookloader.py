import re

from bs4 import BeautifulSoup
from logs import LOGGER

from book import Book


class BookLoader:
    """ Description of a book """
    def __init__(self, url, session):

        self.site_url = 'http://books.toscrape.com/'
        self.page_url = url
        self.session = session
        self.html = self.session.get(self.page_url, timeout=20).content

    def load(self):

        LOGGER.debug('book load: ' + self.page_url)

        root = BeautifulSoup(self.html, 'html.parser')

        # find title and category
        title = root.find('h1').text
        category = root.find('a', href=re.compile('category/books/')).text

        a_book = Book(category, title)
        a_book.page_url = self.page_url

        # find description
        desc = root.find('div', id=re.compile('product_description'))

        if desc is not None:
            desc = desc.next_sibling.next_sibling.text
        else:
            desc = ''
        a_book.product_description = desc

        # find upc
        upc = root.find_all('td')[0].text
        a_book.universal_product_code = upc

        # find available
        get_nbavailable = root.find(
            'p',
            class_='instock availability').text.strip()
        pos_start = len('In stock (')
        pos_end = len(' available)')
        a_book.number_available = int(get_nbavailable[pos_start:-pos_end])

        # find prices
        a_book.price_excluding_tax = float(root.find_all('td')[2].text[1:])
        a_book.price_including_tax = float(root.find_all('td')[3].text[1:])

        # find rating
        a_book.review_rating = root.find('p', class_='star-rating')['class'][1]

        # find url image
        list_rep = root.find('img')['src'].split('/')[2:]
        a_book.image_url = self.site_url + '/'.join(list_rep)

        return a_book
