from playwright.sync_api import Page, Playwright, sync_playwright, expect

def __init__(self, page:Page):
    self.page = page



def checkout_button(self, page):
    self.page.get_by_role("button", name="Check out").click()