# 📚 Books Online Market Analysis

## Description

Welcome to Books Online Market Analysis in Python ! 📊

This project is a price-tracking tool designed to help analyze the book market by scraping data from the <a href="http://books.toscrape.com/">Books to Scrape</a> website. This beta version extracts detailed information about books and stores it in CSV files, along with book cover images, making it easier to follow trends and pricing in different categories.

## Prerequisites

Before starting, ensure you have Python installed on your system.

## Installation

Clone the repository :

```
git clone https://github.com/gabrielgonta/AnalystBooks.git
```

Create and activate a virtual environment :

```
python -m venv env
source env/bin/activate
```

Install the dependencies :

```
cd AnalystBooks
pip install -r requirements.txt
```

## Deployment

Run the scraper :

```
python scrape.py
```

## Usage

To run the program with default settings :

```
python scrape.py
```

If you wish to specify custom directories for CSV and image storage, you can use the following options :

```
python scrape.py --csv-dir <your_csv_directory> --img-dir <your_img_directory>
```

Example :

```
python scrape.py --csv-dir my_csv_folder --img-dir my_img_folder
```

This will save the CSV files in ```my_csv_folde```r and the book images in ```my_img_folder```.

## Key Features

            ✔️ Web Scraping: Extracts book data such as titles, prices, availability, ratings, and category.
            ✔️ CSV Export: Automatically generates a CSV file for each category of books with all relevant data.
            ✔️ Image Download: Saves book cover images in the appropriate category folder.
            ✔️ Flexible Output: You can specify custom directories for both CSV files and images via command line options.

## How It Works

By default, the program will scrape data from all categories of books and store:

CSV files: Generated in the _csv_ directory (one file per category).
Images: Saved in the _img_ directory, organized by category.
Images are named after the first 40 characters of the book title, followed by .png.

## License

This project is licensed under the MIT License.

## Authors

* **Gabriel Gonta** - *Initial work* - [AnalystBooks](https://github.com/gabrielgonta/AnalystBooks.git)