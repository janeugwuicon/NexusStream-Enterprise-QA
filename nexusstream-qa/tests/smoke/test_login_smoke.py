import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from core.base_test import BaseTest

@pytest.mark.smoke
class TestLogin(BaseTest):

    def test_valid_login(self):
        login = LoginPage(self.page)
        inventory = InventoryPage(self.page)

        login.load()
        login.login("standard_user", "secret_sauce")

        expect(inventory.title).to_have_text("Products")