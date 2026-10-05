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

    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        (driver.execute_script('window.scrollTo(0,'
                               'document.body.scrollHeight);'))
        time.sleep(scroll_pause)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height

    titles = driver.find_elements('css selector', 'div.thumbnail a.title ')
    prices = driver.find_elements('css selector', 'div.thumbnail h4.price')
    descriptions = (driver.find_elements('css selector',
                                         'div.thumbnail p.description'))
    ratings = driver.find_elements('css selector', 'div.thumbnail .ratings')

    products = []
    seen = set()

    for title_elem, price_elem, desc_elem, ratings in zip(
      titles, prices, descriptions, ratings):
        title = title_elem.get_attribute('title')
        price = price_elem.text
        description = desc_elem.text
        rating = (len(ratings.find_elements('css selector',
                                            '.ws-icon-star')))

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
