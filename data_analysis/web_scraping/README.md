### 0. Fetch HTML
Write a function def fetch_html(url, headers = None, timeout = 10): that fetches a web page and returns its HTML as text.
### 1. Basic Static Scraping
Write a function def scrape_basic(url): that scrapes the first page of quotes from quotes.toscrape.com.
### 2. Pagination Handling
Write a function def scrape_paginated(base_url): that follows “Next” links on quotes.toscrape.com until no more pages remain
### 3. API-Based Scraping
Write a function def scrape_via_api(base_url): that fetches quote data from all the quotes' API pages
### 4. JSON‑LD Extraction
Write a function def extract_jsonld(url): that pulls quotes from embedded JSON‑LD on a page
### 5. Login & Scrape
Write a function def login_and_scrape(login_url, user, pwd): that logs in and scrapes quotes visible only after authentication
### 6. Scrape Static Products
Write a function def scrape_products(url): that opens a static product category page and returns a list of product dictionaries. Each dict should have
### 7. Scrape Single Product Detail
Write a function def scrape_product_detail(url, delay=2.0) that opens a detail page for one product, waits delay seconds, and returns a dictionary with
