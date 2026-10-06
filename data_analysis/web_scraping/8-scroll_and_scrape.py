#!/usr/bin/env python3
"""
Write a function that scrolls a JS-rendered infinite-scroll page
and extracts all of its products
"""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """
    Scrolls an infinite-scroll page until its height stops increasing,
    waiting up to scroll_pause seconds after each scroll, then returns
    a list of unique product dicts with the product's title, price,
    description, and rating
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.page_load_strategy = 'eager'

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        (driver.execute_script('window.scrollTo(0,'
                               'document.body.scrollHeight);'))
        deadline = time.time() + scroll_pause
        new_height = last_height
        while time.time() < deadline:
            time.sleep(0.1)
            new_height = (driver.execute_script('return '
                                                'document.body.scrollHeight'))
            if new_height > last_height:
                break
        if new_height <= last_height:
            break
        last_height = new_height

    titles = driver.find_elements('css selector', 'div.thumbnail a.title')
    prices = driver.find_elements('css selector', 'div.thumbnail h4.price')
    descriptions = (driver.find_elements('css selector',
                                         'div.thumbnail p.description'))
    ratings = driver.find_elements('css selector', 'div.thumbnail .ratings')

    products = []
    seen = set()

    for title_elem, price_elem, desc_elem, rating_block in zip(
      titles, prices, descriptions, ratings):
        title = title_elem.get_attribute('title')
        price = price_elem.text

        key = (title, price)
        if key not in seen:
            seen.add(key)
            description = desc_elem.text
            rating = (len(rating_block.find_elements('css selector',
                                                     '.ws-icon-star')))
            products.append({
                'title': title,
                'price': price,
                'description': description,
                'rating': rating
            })

    driver.quit()
    return products
