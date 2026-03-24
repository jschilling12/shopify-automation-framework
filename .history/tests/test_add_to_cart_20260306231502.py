import re
import pytest
from playwright.sync_api import Page, expect
from pages.add_to_cart_page import AddToCartPage

def add_to_cart(page:Page) -> None:
    page.goto("https://gamedaytldr.live/")
    cart_flow = AddToCartPage(page)
    cart_flow.add_to_cart('jcschill12@gmail.com', 'USA', 'Arsenal')
