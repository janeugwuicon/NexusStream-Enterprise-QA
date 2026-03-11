from .base_page import BasePage


class ProductPage(BasePage):

    SEARCH = "#search_product"
    SEARCH_BTN = "#submit_search"
    ADD_CART = ".add-to-cart"
    VIEW_CART = "u:has-text('View Cart')"

    def search_product(self, name):

        self.fill(self.SEARCH, name)
        self.click(self.SEARCH_BTN)

    def add_first_product(self):

        self.page.locator(self.ADD_CART).first.click()
        self.click(self.VIEW_CART)