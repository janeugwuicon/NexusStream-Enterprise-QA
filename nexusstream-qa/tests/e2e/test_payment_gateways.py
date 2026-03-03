import csv
import pytest
from pathlib import Path
from playwright.sync_api import expect
from pages.checkout_page import CheckoutPage

def load_csv_data():
    """Reads test data safely, completely ignoring what the headers are named."""
    file_path = Path(__file__).parent.parent.parent / "data" / "credit_cards.csv"
    
    with open(file_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.reader(f) # Using standard reader to avoid KeyError!
        next(reader)           # Skip the header row completely
        
        # Grab the 1st column [0] and 2nd column[1]
        return [
            (row[0].strip(), row[1].strip()) 
            for row in reader 
            if len(row) >= 2   # Skip any blank lines at the bottom of the file
        ]

@pytest.mark.parametrize("card_number, expected_status", load_csv_data())
def test_payment_zip_injection(auth_page, card_number, expected_status):
    auth_page.goto("https://www.saucedemo.com/checkout-step-one.html")
    checkout = CheckoutPage(auth_page)
    
    checkout.zip_code_input.fill(card_number)
    expect(checkout.zip_code_input).to_have_value(card_number)