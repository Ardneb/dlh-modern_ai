#!/usr/bin/env python3
"""Function fetches a web page and returns its HTML as text"""

import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch website from URL and return text"""
    response = requests.get(url)
    response.raise_for_status()
    return response.text
