class Category:
    """ manage a collection of books """

    def __init__(self, name):
        self.category_name = name
        self.category_page1_url = ''
        self.books = []

    def add_book(self, book):
        # if the book exists change the version of the book before add
        if book in self.books:
            book.add_version()
        self.books.append(book)

    def __str__(self):
        return self.category_name + ': (' + str(len(self.books)) + ' books)'

    def __repr__(self):
        info = '\n'.join([
            f'name: {self.category_name}',
            f'page: {self.category_page1_url}',
            f'books:'
        ])
        info += '\n' + '\n'.join([str(c) for c in self.books])
        return info


