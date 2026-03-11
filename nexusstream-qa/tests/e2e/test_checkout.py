import uuid
from playwright.sync_api import expect


def test_checkout_e2e(page, signup, products, checkout):

    email = f"user_{uuid.uuid4().hex[:6]}@test.com"

    # create account
    signup.open("/login")
    signup.create_account("Jane", email)
    signup.continue_login()

    # search product
    products.open("/products")
    products.search_product("Blue Top")

    # add to cart
    products.add_first_product()

    # checkout steps
    checkout.proceed_to_checkout()
    checkout.add_order_message("Deliver during working hours")
    checkout.place_order()

    # payment
    checkout.pay(
        "Jane Doe",
        "4111111111111111",
        "123",
        "12",
        "2030"
    )

    # assertion
    expect(page.locator(checkout.SUCCESS)).to_be_visible(timeout=10000)