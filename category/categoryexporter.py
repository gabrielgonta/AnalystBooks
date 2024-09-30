import csv
import os
import string
from logs import LOGGER
from book import BookExporter


class CategoryExporter:
    """ Export the collection of books of a category to a csv file """
    def __init__(self, category):
        self.category = category

    def to_csv(self, file):
        LOGGER.debug('Export to csv file')

        with open(file, 'w', newline='', encoding='utf-8') as f:

            output = csv.writer(f, delimiter=',')

            output.writerow([
                'product_page_url',
                'universal_ product_code (upc)',
                'title',
                'price_including_tax',
                'price_excluding_tax',
                'number_available',
                'product_description',
                'category',
                'review_rating',
                'image_url'
            ])

            for a_book in self.category.books:
                book_to_csv = BookExporter(a_book)
                book_to_csv.to_csv(f)

    def export_pictures(self, directory, session):
        """ export all the pictures of the category """
        # create the folder for the category
        category_path = directory + '/' + self.category.category_name.replace(' ', '_')
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # export the pictures of the books
        for book in self.category.books:
            # define the name of the file
            file_name = category_path \
                        + '/' + book.title_modify \
                        + '_' + book.version \
                        + '.png'

            book.image_file = file_name
            book_exporter = BookExporter(book)
            book_exporter.export_pictures(session)

        # export new csv
        self.to_csv(category_path + '/' + self.category.category_name + '.csv')
