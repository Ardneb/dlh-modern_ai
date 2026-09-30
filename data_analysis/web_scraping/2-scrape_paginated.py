#!/usr/bin/env python3
"""
Write a function that follows “Next” links on
quotes.toscrape.com until no more pages remain
"""

from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """
    Fetch quotes website and scrape all pages
    extracting the quote text, the author and tags
    """
    scraped_quotes = []
    next_page_url = base_url

    while next_page_url:
        html = fetch_html(next_page_url)
        soupobject = BeautifulSoup(html, 'html.parser')

        # Scrape quotes from the current page
        quotes_on_page = scrape_basic(html)
        scraped_quotes.extend(quotes_on_page)

        # Find the "Next" link
        next_link = soupobject.find('li', class_='next')
        if next_link:
            next_page_relative_url = next_link.find('a')['href']
            next_page_url = parse.urljoin(base_url, next_page_relative_url)
            time.sleep(1)  # Be polite and avoid overwhelming the server
        else:
            next_page_url = None  # No more pages to scrape

    return scraped_quotes
