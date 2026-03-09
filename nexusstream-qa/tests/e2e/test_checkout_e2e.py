import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.mark.e2e
def test_checkout_e2e(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    login.load()
    login.login("standard_user", "secret_sauce")

    page.goto("/inventory.html")

    inventory.search_and_add("sauce-labs-backpack")
    expect(inventory.cart_badge).to_have_text("1")

    inventory.go_to_cart()
    checkout.start_checkout()

    checkout.fill_shipping("John", "Doe", "12345")

    confirmation = checkout.finish()
    expect(confirmation).to_have_text("Thank you for your order!")