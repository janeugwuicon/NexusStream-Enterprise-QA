import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from core.builders import UserBuilder

@pytest.mark.e2e
def test_complete_checkout(auth_page):

    inventory = InventoryPage(auth_page)
    checkout = CheckoutPage(auth_page)

    auth_page.goto("https://www.saucedemo.com/inventory.html")

    inventory.add_item("sauce-labs-backpack")
    expect(inventory.cart_badge).to_have_text("1")

    inventory.open_cart()
    checkout.start_checkout()

    user = UserBuilder().build()
    checkout.fill_shipping(*user)
    checkout.finish()

    expect(checkout.success_header).to_have_text("Thank you for your order!")