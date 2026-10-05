#!/usr/bin/env python3
"""
Write a function that opens a detail page for one
product, waits delay seconds, and returns a dictionary with
"""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
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
    time.sleep(delay)  # Wait for the page to load

    title = driver.find_element('css selector', '.caption h4')[1].text
    price = driver.find_element('css selector', 'h4.price').text
    description = driver.find_element('css selector', 'p.description').text
    rating = (len(driver.find_element('css selector',
                                      '.ratings p.ws-icon.ws-icon-star')))

    driver.quit()

    return {
        'title': title,
        'price': price,
        'description': description,
        'rating': rating
    }
