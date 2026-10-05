#!/usr/bin/env python3
"""
Write a function that opens a detail page for one
product, waits delay seconds, and returns a dictionary with
"""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """
    Opens a detail page for one product, waits delay seconds,
    and returns a dictionary with the product's title, price,
    description, and rating
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(scroll_pause)

    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        (driver.execute_script('window.scrollTo(0,'
                               'document.body.scrollHeight);'))
        time.sleep(scroll_pause)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height

    products = []
    seen = set()
    product_cards = driver.find_elements('css selector', 'div.thumbnail')

    for card in product_cards:
        title = ((card.find_element('css selector',
                                    'a.title').get_attribute('title')))
        price = card.find_element('css selector', 'h4.price').text
        description = card.find_element('css selector', 'p.description').text
        rating = (len(card.find_elements('css selector',
                                         '.ratings .ws-icon-star')))

        key = (title, price)
        if key not in seen:
            seen.add(key)
            products.append({
                'title': title,
                'price': price,
                'description': description,
                'rating': rating
            })

    driver.quit()
    return products
