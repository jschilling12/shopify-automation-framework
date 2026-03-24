import sys
import os
import pytest
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))

# Pytest fixture for Playwright page object, to be used across all tests.

@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://gamedaytldr.live/")
        yield page
        context.close()
        browser.close()