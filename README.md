# Movie Scraper

A Python script to scrape movie links from the website [f2mex.ir](https://www.f2mex.ir/) based on user-defined IMDb ratings. The script allows users to specify a minimum IMDb rating and the number of pages to explore for movies.

## Features

- Asks the user for a minimum IMDb rating.
- Allows the user to specify the number of pages to scrape.
- Collects and displays movie links with ratings above the specified threshold.
- Outputs the title of each movie alongside the corresponding links.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup4` library
- `re` library (part of the standard library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/moviescraper.git
   cd moviescraper

## Example   
   ```bash
   Enter the IMDb rating you want to be higher: 6
Enter the number of pages that you want to explore: 3
Movie Title 1
Movie Title 2
...
Movie Title N
