import re
import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect
from pages.add_to_cart_page import AddToCartPage

def test_add_to_cart(page:Page, playwright: Playwright) -> None:: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gamedaytldr.live/")
    cart_flow = AddToCartPage(page)
    cart_flow.add_to_cart('jcschill12@gmail.com', 'USA', 'Arsenal')

