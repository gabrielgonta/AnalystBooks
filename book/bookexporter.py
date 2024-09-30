import csv
import requests
import os
from logs import LOGGER


class BookExporter:
    """ Export a book in a csv file """
    def __init__(self, book):
        self.book = book

    def to_csv(self, file):

        LOGGER.debug('export ' + str(self.book))

        output = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

        if self.book.image_file:
            image_file = self.book.image_file
        else:
            image_file = self.book.image_url

        data = [
                self.book.page_url,
                self.book.universal_product_code,
                self.book.title,
                self.book.price_including_tax,
                self.book.price_excluding_tax,
                self.book.number_available,
                self.book.product_description,
                self.book.category,
                self.book.review_rating,
                image_file
        ]

        output.writerow([str(d).encode('utf-8').decode('utf-8') for d in data])

    def export_pictures(self, session):

        LOGGER.debug(' Load image: ' + self.book.image_url)
        r = session.get(self.book.image_url, timeout=20).content

        # save the file
        with open(self.book.image_file, "wb+") as f:
            f.write(r)

