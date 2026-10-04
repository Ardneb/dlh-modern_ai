#!/usr/bin/env python3
"""
Write a function that logs in and scrapes
quotes visible only after authentication
"""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """
    Logs in to the quotes website and scrapes
    """
    session = requests.Session()

    soup = BeautifulSoup(session.get(login_url).text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

    payload = {
        'username': user,
        'password': pwd,
        'csrf_token': csrf_token
    }
    session.post(login_url, data=payload)

    protected_response = session.get("https://quotes.toscrape.com/")
    quotes_soup = BeautifulSoup(protected_response.text, 'html.parser')

    quotes = []
    for block in quotes_soup.find_all('div', class_='quote'):
        text = block.find('span', class_='text').get_text(strip=True)
        author = block.find('small', class_='author').get_text(strip=True)
        tags = ([tag.get_text(strip=True)
                for tag in block.find_all('a', class_='tag')])

        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    return quotes
