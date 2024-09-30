import app
import argparse
from logs import LOGGER
from .parameters import Parameters


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser('books_to_scrape')

        self.parser.add_argument('--version', '-v',
                                 action='store_true',
                                 help='show current version')

        self.parser.add_argument('--csv-dir',
                                 type=str,
                                 help='set the csv files directory')

        self.parser.add_argument('--img-dir',
                                 type=str,
                                 help='set the image files directory')

        self.args = self.parser.parse_args()

        LOGGER.debug(self.args)

        if self.args.version:
            print('books_to_scrape ' + app.__version__)

    def read_parameters(self):

        p = Parameters()

        if self.args.csv_dir is not None:
            p.csv_directory = self.args.csv_dir

        if self.args.img_dir is not None:
            p.img_directory = self.args.img_dir

        return p
