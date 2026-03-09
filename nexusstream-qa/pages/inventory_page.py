from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")

    def search_and_add(self, product_id: str):
        self.page.get_by_test_id(f"add-to-cart-{product_id}").click()

    def go_to_cart(self):
        self.page.get_by_test_id("shopping-cart-link").click()