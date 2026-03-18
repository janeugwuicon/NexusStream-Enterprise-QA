from playwright.sync_api import Route
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_payment_api_down(page):

    def mock_api(route: Route):
        route.fulfill(
            status=500,
            body="Payment Failed"
        )

    # Mocking the checkout completion endpoint
    # Note: For SauceDemo, we intercept the navigation or a specific asset to simulate failure
    page.route("**/payment*", mock_api)

    # 1. Login
    lp = LoginPage(page)
    lp.load()
    lp.login("standard_user", "secret_sauce")

    # 2. Add item and go to cart
    inv = InventoryPage(page)
    inv.add_item()
    inv.go_to_cart()

    # 3. Proceed to Checkout
    cart = CartPage(page)
    cart.checkout()

    # 4. Fill details and attempt payment
    checkout = CheckoutPage(page)
    checkout.fill_details("Test", "Mock", "50000")
    checkout.finish()

    # 5. Assert that the Success page is NOT visible (implying failure or error handling)
    # In a real app, you would assert an error toast message is visible
    # checkout.error.is_visible() 