import re
import pytest
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    try:
        page.goto("https://gamedaytldr.live/")
    except Exception as e:
        print(f"Error occurred while navigating to the page: {e}")
        
    try:
        page.get_by_label("data-wc-card", name="promo-option-card-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").click()
    except Exception as e:
        print(f"Error occurred while clicking the link: {e}")


# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="promo-option-card-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# promo-option-card-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9 selected