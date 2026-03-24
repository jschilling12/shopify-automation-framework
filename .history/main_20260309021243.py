from tests.test_frontend import test_add_to_cart
from playwright.sync_api import Page, Playwright, sync_playwright, expect


test_add_to_cart(page:Page, playwright: Playwright)