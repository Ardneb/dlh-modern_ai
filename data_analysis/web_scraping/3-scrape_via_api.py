#!/usr/bin/env python3
"""
Write a function that fetches that fetches
quote data from all the quotes' API pages
"""

import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """
    Fetch quotes website and scrape all pages
    extracting the quote text, the author and tags
    """
    all_quotes = []
    page_number = 1
    base_url = base_url.rstrip('/')

    while True:
        endpoint = f"{base_url}/api/quotes?page={page_number}"

        # Retrieve the JSON payload string and
        # parse it into a Python dictionary
        json_payload = fetch_html(endpoint)
        data = json.loads(json_payload)

        # Process each quote from the current API page
        quotes_on_page = data.get('quotes', [])
        for item in quotes_on_page:
            # Handle author wheter returned as a string or a dictionary
            author = item.get('author')
            author_name = (author.get('name')
                           if isinstance(author, dict) else author)

            all_quotes.append({
                'text': item.get('text'),
                'author': author_name,
                'tags': item.get('tags', [])
            })

        # Stop after the last page
        if not data.get('has_next'):
            break

        page_number += 1

    return all_quotes
