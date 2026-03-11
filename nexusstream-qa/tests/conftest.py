import pytest
from pages.signup_page import SignupPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage


@pytest.fixture
def signup(page):
    return SignupPage(page)


@pytest.fixture
def products(page):
    return ProductPage(page)


@pytest.fixture
def checkout(page):
    return CheckoutPage(page)


@pytest.fixture
def login(page):
    return LoginPage(page)