from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_success(page):
    lp = LoginPage(page)
    lp.load()
    lp.login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    inv.add_item()
    inv.go_to_cart()

    cart = CartPage(page)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.fill_details("Jane", "QA", "10001")
    checkout.finish()

    assert checkout.success.is_visible()
    

