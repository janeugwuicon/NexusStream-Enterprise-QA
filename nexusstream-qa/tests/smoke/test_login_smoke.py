import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.smoke
def test_login_smoke(page):
    login = LoginPage(page)
    home = HomePage(page)

    login.load()
    login.login("standard_user", "secret_sauce")

    expect(home.title).to_have_text("Products")