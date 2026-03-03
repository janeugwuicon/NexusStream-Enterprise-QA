from core.base_page import BasePage

class InventoryPage(BasePage):

    @property
    def title(self):
        return self.page.locator(".title")

    @property
    def cart_badge(self):
        return self.by_test_id("shopping-cart-badge")

    def add_item(self, product_id: str):
        self.by_test_id(f"add-to-cart-{product_id}").click()

    def open_cart(self):
        self.by_test_id("shopping-cart-link").click()