import re
import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect
from pages.add_to_cart_page import AddToCartProcess
from pages.checkout_page import CheckoutProcess
from checkout_selectors import CheckoutSelectors
from addtocart_selectors import AddtocartSelectors

# Orchestration layer for Pytest functions

BASE_URL = "https://gamedaytldr.live/"

# World Cup Team
TEXT_TEAMNAME = 'USA'

# Dropdown for Premier League team
DROPDOWN = 'Arsenal'
EMAIL = 'fakeeamil@gmail.com'
NUM = '1'
EXP = '03/30'
SEC = '111'
NAME = '1'
FIRST = 'Jordan'
LAST = 'Schilling'
CUSTOMER_ADDRESS = '111'

# Selection for address dropdown
CUSTOMER_ADDRESS_OPTIONS = '111 North Orange Ave'

add_to_cart_sel = AddtocartSelectors(
    selection_input= ".promo-option-indicator-" \
        "aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    selection_input_promo= ".promo-option-card-" \
        "aodrsmzfpyxdet0hvraigenblock388c186ytkrd9.is-radio > " \
        ".promo-option-inner-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9 > "
        ".promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    promo_toggle=".epl-optin-toggle-checkbox-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    promo_body ="#epl-body-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    promo_email="#epl-email-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    email= "Email Address *",
    team= "Favourite Team *",
    dropdown= "Favourite EPL Team *",
    cart= "Add to Cart"
)

checkout_sel = CheckoutSelectors(
    add_to_cart="Add to Cart",
    checkout="Check out",
    account="Email",
    card_number_frame='iframe[name^="card-fields-number-"]',
    exp_date_frame='iframe[name^="card-fields-expiry-"]',
    sec_code_frame='iframe[name^="card-fields-verification_value-"]',
    card_name_frame='iframe[name^="card-fields-name-"]',
    customer_name_first="First name",
    customer_name_last="Last name",
    customer_address="Address",
    pay="Pay now",
    homepage="Continue shopping",
)

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