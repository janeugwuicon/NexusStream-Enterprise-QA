import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("fname, lname, zip_code", [
    ("", "Doe", "10001"),    # Missing First Name
    ("Jane", "", "10001"),   # Missing Last Name
    ("Jane", "Doe", ""),     # Missing Postal Code
    ("", "", "")             # All Empty
])
def test_checkout_empty_fields(page, fname, lname, zip_code):
    lp = LoginPage(page)
    lp.load()
    lp.login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    inv.add_item()
    inv.go_to_cart()

    cart = CartPage(page)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.fill_details(fname, lname, zip_code)

    assert checkout.error.is_visible()
