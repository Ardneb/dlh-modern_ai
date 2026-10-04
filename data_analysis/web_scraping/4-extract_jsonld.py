#!/usr/bin/env python3
"""
Write a function that pulls quotes
from embedded JSON‑LD on a page
"""

import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """
    Fetches a web page and extracts quotes
    embedded within JSON-LD blocks
    """
    html = fetch_html(url)
    soup= BeautifulSoup(html, 'html.parser')

    quotes = []

    for script in soup.find_all('script', type='application/ld+json'):
        data = json.loads(script.string)

        # Check if the JSON-LD data is a list or a single object
        items = data if isinstance(data, list) else [data]

        for item in items:
            if item.get('@type') == 'Quote':
                text = item.get('text')
                author = item.get('author', {}).get('name')
                keywords = item.get('keywords', '')
                tags = (keywords.split(',') 
                        if isinstance(keywords, str) else keywords)
                quotes.append({
                    'text': text,
                    'author': author,
                    'tags': tags
                })

    return quotes
