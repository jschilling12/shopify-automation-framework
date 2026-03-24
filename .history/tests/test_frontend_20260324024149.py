import re
import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect
from pages.add_to_cart_page import AddToCartProcess
from pages.checkout_page import CheckoutProcess


# Orchestration layer for Pytest functions


def test_add_to_cart(page:Page, playwright: Playwright, email, text_teamname, dropdown):
    cart_flow = AddToCartProcess(page, add_to_cart_sel)
    cart_flow.add_to_cart(email, text_teamname, dropdown)

def test_checkout(page:Page, playwright: Playwright, 
        text_teamname, dropdown, email, num, exp, sec, name, 
        first, last, customer_address, customer_address_option):
    cart_flow = AddToCartProcess(page, add_to_cart_sel)
    cart_flow.add_to_cart(email, text_teamname, dropdown)
    checkout = CheckoutProcess(page, checkout_sel)
    checkout.checkout(email, num, exp, sec, name, first, last, 
        customer_address, customer_address_option)
    # expect(page.get_by_role("button", name="Pay now")).to_be_visible()