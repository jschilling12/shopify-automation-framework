from playwright.sync_api import Page, expect

class AddToCartPage:
    def __init__(self, page:Page):
        self.page = page
        self.selection_input = page.locator(".promo-option-indicator-" \
        "aodrsmzfpyxdet0hvraigenblock388c186ytkrd9")
        self.selection_input_promo = page.locator(".promo-option-card-" \
        "aodrsmzfpyxdet0hvraigenblock388c186ytkrd9.is-radio > " \
        ".promo-option-inner-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9 > "
        ".promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9")
        self.email = page.get_by_role("textbox", name="Email Address *")
        self.team_textbox = page.get_by_role("textbox", name="Favourite Team *")
        self.team_dropdown = page.get_by_label("Favourite EPL Team *")
        self.cart = page.get_by_role("button", name="Add to Cart")

    def select_input(self):
        self.selection_input.first.click()

    def select_input_promo(self, page):
        self.page.locator(".epl-optin-toggle-checkbox-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").click()
        self.selection_input_promo.first.click()

    def input_email(self, email, page):
        self.page.get_by_text("✉️ Email").first.click()
        self.email.fill(email)
    
    def input_email_promo(self, email):
        self.page.locator("#epl-body-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9").get_by_text("✉️ Email").click()
        self.email.fill(email)

    def input_team(self, text_teamname):
        self.team_textbox.fill(text_teamname)

    def select_team(self, teamname):
        self.team_dropdown.select_option(teamname)
    
    def select_cart(self):
        self.cart.click()

    def add_to_cart(self, email, text_teamname, teamname, page):
        self.select_input()
        self.input_email(email, page)
        self.input_team(text_teamname)
        self.select_input_promo(page)
        self.input_email_promo(email)
        self.select_team(teamname)