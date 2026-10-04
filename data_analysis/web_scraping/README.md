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
