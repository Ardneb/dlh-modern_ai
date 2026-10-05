#!/usr/bin/env python3
"""Scrape every product from a JS-rendered infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """
    Open url in headless Chrome, scroll to the bottom repeatedly until
    the page height stops growing, then extract every div.thumbnail
    product card.

    Returns a list of unique dicts with the keys title, price,
    description and rating. Duplicates are detected on (title, price).
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    products = []
    seen = set()

    try:
        driver.get(url)

        last_height = driver.execute_script(
            'return document.body.scrollHeight')
        while True:
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')

            new_height = last_height
            deadline = time.time() + scroll_pause
            while time.time() < deadline:
                time.sleep(0.1)
                new_height = driver.execute_script(
                    'return document.body.scrollHeight')
                if new_height != last_height:
                    break

            if new_height == last_height:
                break
            last_height = new_height

        for card in driver.find_elements('css selector', 'div.thumbnail'):
            links = card.find_elements('css selector', 'a.title')
            prices = card.find_elements('css selector', 'h4.price')
            descs = card.find_elements('css selector', 'p.description')
            stars = card.find_elements(
                'css selector', '.ratings p.ws-icon-star')

            if not links or not prices:
                continue

            title = links[0].get_attribute('title')
            price = prices[0].text
            key = (title, price)
            if key in seen:
                continue
            seen.add(key)

            products.append({
                'title': title,
                'price': price,
                'description': descs[0].text if descs else '',
                'rating': len(stars),
            })
    finally:
        driver.quit()

    return products
