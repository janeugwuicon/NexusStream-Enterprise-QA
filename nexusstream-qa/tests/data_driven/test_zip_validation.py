import csv
from pathlib import Path
import pytest
from pages.checkout_page import CheckoutPage

def load_data():
    path = Path(__file__).parents[2] / "data" / "credit_cards.csv"
    with open(path, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)
        return [(row[0], row[1]) for row in reader if len(row) >= 2]

@pytest.mark.parametrize("zip_code, expected", load_data())
def test_zip_field(auth_page, zip_code, expected):
    auth_page.goto("https://www.saucedemo.com/checkout-step-one.html")
    checkout = CheckoutPage(auth_page)
    checkout.zip_code_input.fill(zip_code)
    assert checkout.zip_code_input.input_value() == zip_code