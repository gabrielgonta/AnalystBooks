from category import Category
from book import BookLoader
from logs import LOGGER
from bs4 import BeautifulSoup


class CategoryLoader:
    """ generate a category whith a collection of books """
    def __init__(self, session, url):
        self.session = session
        self.page_url = url
        self.page_url_index = '/index.html'
        self.html = self.session.get(self.page_url + self.page_url_index).content
        self.main_url = 'http://books.toscrape.com/catalogue/'
        self.root = BeautifulSoup(self.html, 'html.parser')
        self.page_count = self.get_page_count()

    def load(self):
        """ load all the pages of the category """
        # read the name of category
        name = self.root.find('h1').text

        cat = Category(name)
        cat.category_page1_url = self.page_url

        return self.load_all_pages(cat)

    def get_page_count(self):
        """ give the number of pages of the category """
        nb = 1
        li = self.root.find('li', class_='current')
        if li is not None:
            nb = int(li.text.strip().split(' ')[3])
        return nb

    def load_all_pages(self, cat):
        """ call load_books for each page """
        LOGGER.debug('Category loader for ' + str(self.page_count) + ' pages')
        for p in range(1, self.page_count + 1):
            if p == 1:
                self.page_url_index = '/index.html'
            else:
                self.page_url_index = f'/page-{p}.html'
            self.load_all_books(p, cat)
        return cat

    def load_all_books(self, page, cat):
        """ call the book loader for each book of the page """
        self.html = self.session.get(self.page_url + self.page_url_index, timeout=20).content
        LOGGER.debug('Category load page ' + str(page) + ': ' + self.page_url + self.page_url_index)
        self.root = BeautifulSoup(self.html, 'html.parser')

        ol = self.root.find('ol')

        # read the books
        for li in ol.find_all('li'):
            book_url = li.find('a')['href'].split('/')[3:]
            book_url = self.main_url + '/'.join(book_url)

            book_loader = BookLoader(book_url, self.session)
            a_book = book_loader.load()

            cat.add_book(a_book)

        return cat
