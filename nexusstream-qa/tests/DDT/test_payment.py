import csv
import pytest
from playwright.sync_api import expect


def load_cards():

    with open("data/credit_cards.csv") as f:
        return list(csv.DictReader(f))


@pytest.mark.parametrize("card", load_cards())
def test_payment(page, checkout, card):

    page.goto("https://automationexercise.com/payment")

    checkout.pay(
        card["name"],
        card["card_no"],
        card["cvc"],
        card["month"],
        card["year"]
    )

    if card["expected"] == "success":
        expect(page.locator(checkout.SUCCESS)).to_be_visible()