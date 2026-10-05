#!/usr/bin/env python3
"""
Write a function that opens a static product category page
and returns a list of product dictionaries. Each dict should have
"""

import time
from selenium import webdriver


def scrape_products(url):
    """
    Opens a static product category page and
    returns a list of product dictionaries
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    products = []
    product_cards = driver.find_elements('class name', 'thumbnail')

    for card in product_cards:
        title = (card.find_element('css selector',
                                   'a[title]').get_attribute('title'))
        price = card.find_element('class name', 'price').text
        description = card.find_element('class name', 'description').text

        rating_elem = (card.find_element('css selector',
                                         '.ratings p[data-rating]'))
        rating = int(rating_elem.get_attribute('data-rating'))

        products.append({
            'title': title,
            'price': price,
            'description': description,
            'rating': rating
        })

    driver.quit()
    return products
