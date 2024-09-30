import logging
import sys


class Logger:
    """ Manage the logs of the project """
    def __init__(self):

        self.logger = logging.getLogger('books_to_scrape')

        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        formatter = logging.Formatter("---> %(message)s")
        console.setFormatter(formatter)
        self.logger.addHandler(console)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s "
            "- %(message)s", "%d/%m/%Y %H:%M:%S")
        file_handler = logging.FileHandler("logs/scrape.log", encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        logging.basicConfig(level=logging.DEBUG, handlers=[])

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
