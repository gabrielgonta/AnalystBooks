import textwrap
import string

class Book:
    def __init__(self, category, title):
        self.page_url = ''
        self.universal_product_code = ''
        self.title = title
        self.product_description = ''
        self.category = category
        self.price_including_tax = 0
        self.price_excluding_tax = 0
        self.number_available = 0
        self.review_rating = 0
        self.image_url = ''

        # attribute used for png creation
        self.version = 'V1'
        # only the 40 first caracters without punctuation and quote
        self.title_modify = self.title[:40].translate(
            str.maketrans('', '', string.punctuation)).replace("’", ' ')
        self.image_file = ''

    def __str__(self):
        return '[' + self.category + '] ' + self.title

    def __repr__(self):
        return '\n'.join([
            f'title: {self.title} - {self.version}',
            f'Modify title: {self.title_modify}',
            f'category: {self.category}',
            f'page: {self.page_url}',
            f'description: '
            f'{textwrap.fill(self.product_description, width=150)}',
            f'universal product code: {self.universal_product_code}',
            f'price (tax): {self.price_including_tax}',
            f'price (no tax): {self.price_excluding_tax}',
            f'number available: {self.number_available}',
            f'review rating: {self.review_rating}',
            f'image url: {self.image_url}'
        ])

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title_modify == other.title_modify
        else:
            return False

    def add_version(self):
        self.version = 'V' + str(int(self.version[1])+1)
