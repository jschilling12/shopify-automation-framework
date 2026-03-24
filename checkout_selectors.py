from dataclasses import dataclass

# Config

@dataclass
class CheckoutSelectors:
    add_to_cart: str
    checkout: str
    account: str
    card_number_frame: str
    exp_date_frame: str
    sec_code_frame: str
    card_name_frame: str
    customer_name_first: str
    customer_name_last: str
    customer_address: str
    pay: str
    homepage: str