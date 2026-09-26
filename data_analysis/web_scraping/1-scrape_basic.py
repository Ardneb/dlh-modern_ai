#!/usr/bin/env python3
"""Function scrapes the first page of quotes from given url"""

from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """
    Fetch quotes website and scrape first page
    extracting the quote text, the author and tags
    """
    html = fetch_html(url)                          # already a string
    soupobject = BeautifulSoup(html, 'html.parser')

    scraped_quotes = []
    quote_blocks = soupobject.find_all('div', class_='quote')
    for block in quote_blocks:
        text = block.find('span', class_='text')
        author = block.find('small', class_='author')
        tags = block.find_all('a', class_='tag')

        scraped_quotes.append({
            'text': text.get_text(strip=True) if text else None,
            'author': author.get_text(strip=True) if author else None,
            'tags': [tag.get_text(strip=True) for tag in tags]
        })

    return scraped_quotes
