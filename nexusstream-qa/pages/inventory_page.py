class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart = page.locator(".inventory_item button").first
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_item(self):
        self.add_to_cart.click()

    def go_to_cart(self):
        self.cart_icon.click()