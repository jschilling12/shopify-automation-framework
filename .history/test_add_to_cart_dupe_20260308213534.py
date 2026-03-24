import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gamedaytldr.live/")
    page.locator(".promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").first.click()
    # page.get_by_text("✉️ Email").first.click()
    page.get_by_role("textbox", name="Email Address *").click()
    page.get_by_role("textbox", name="Email Address *").fill("test@gmail.com")
    page.get_by_role("textbox", name="Favourite Team *").click()
    page.get_by_role("textbox", name="Favourite Team *").press("CapsLock")
    page.get_by_role("textbox", name="Favourite Team *").fill("USA")
    page.get_by_role("textbox", name="Favourite Team *").press("CapsLock")
    page.locator(".epl-optin-toggle-checkbox-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").click()
    page.locator(".promo-option-card-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9.is-radio > .promo-option-inner-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9 > .promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").first.click()
    page.locator("#epl-body-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").get_by_text("✉️ Email").click()
    page.locator("#epl-email-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").click()
    page.locator("#epl-email-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").fill("test@gmail.com")
    page.get_by_label("Favourite EPL Team *").select_option("Arsenal")
    page.get_by_role("button", name="Add to Cart").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
