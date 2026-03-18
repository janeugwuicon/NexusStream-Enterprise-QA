from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_btn = page.locator("#checkout")

    def checkout(self):
        self.click(self.checkout_btn)