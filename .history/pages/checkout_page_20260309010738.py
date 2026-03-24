from playwright.sync_api import Page, expect

class CheckoutProcess:
    def __init__(self, page:Page):
        self.page = page
        self.checkout = page.get_by_role("button", name="Add to Cart")
        self.account = page.get_by_role("textbox", name="Email")
        self.card_number = page.locator("iframe[name=\"card-fields-number-kkbywihp4q000000\"]").content_frame.get_by_role("textbox", name="Card number")
        self.exp_date = page.locator("iframe[name=\"card-fields-expiry-m3xllra939d00000\"]").content_frame.get_by_role("textbox", name="Expiration date (MM / YY)")
        self.sec_code = page.locator("iframe[name=\"card-fields-verification_value-b6havdotplk00000\"]").content_frame.get_by_role("textbox", name="Security code")
        self.card_name = page.locator("iframe[name=\"card-fields-name-4h06ew0zdjq00000\"]").content_frame.get_by_role("textbox", name="Name on card")
        self.customer_name_first = page.get_by_role("textbox", name="First name")
        self.customer_name_last = page.get_by_role("textbox", name="Last name")
        self.customer_address = page.get_by_role("combobox", name="Address")
        self.pay = page.get_by_role("button", name="Pay now")
        self.homepage = page.get_by_role("link", name="Continue shopping")
    
    def checkout_button(self):
        self.checkout.click()

    def account_email(self, email):
        self.account.click()
        self.account.fill(email)

    def card_details(self, num, exp, sec, name ):
        self.card_number.click()
        self.card_number.fill(num)
        self.exp_date.click()
        self.exp_date.fill(exp)
        self.sec_code.click()
        self.sec_code.fill(sec)
        self.card_name.click()
        self.card_name.fill(name)

    def customer_details(self, first, last):
        self.customer_name_first.click()
        self.customer_name_first.fill(first)
        self.customer_name_last.click()
        self.customer_name_last.fill(last)
        self.customer_address.click()
        self.customer_address.fill("111")
        self.page.get_by_role("option", name="111 North Orange Avenue,").click()
    
    def pay_now(self):
        self.pay.click()

    def continue_shopping(self):
        self.homepage.click()

    def checkout_flow(self, email, num, exp, sec, name, first, last):
        self.checkout_button()
        self.account_email(email)
        self.card_details(num, exp, sec, name)
        self.customer_details(first, last)
        self.pay_now()
        self.continue_shopping()
    