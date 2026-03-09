import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


checkout_validation_cases = [
    pytest.param("", "User", "12345", "Error: First Name is required", id="missing-first-name"),
    pytest.param("Test", "", "12345", "Error: Last Name is required", id="missing-last-name"),
    pytest.param("Test", "User", "", "Error: Postal Code is required", id="missing-postal-code"),
]


@pytest.mark.parametrize("first_name, last_name, postal_code, expected_error", checkout_validation_cases)
def test_checkout_form_validation_errors(page: Page, first_name: str, last_name: str, postal_code: str, expected_error: str):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.search_and_add("sauce-labs-backpack")
    inventory_page.go_to_cart()
    checkout_page.start_checkout()

    checkout_page.fill_shipping(first_name, last_name, postal_code)

    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text(expected_error)