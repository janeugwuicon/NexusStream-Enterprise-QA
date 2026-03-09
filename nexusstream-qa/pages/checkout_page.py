from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def start_checkout(self):
        self.page.get_by_test_id("checkout").click()

    def fill_shipping(self, first, last, zip_code):
        self.page.get_by_test_id("firstName").fill(first)
        self.page.get_by_test_id("lastName").fill(last)
        self.page.get_by_test_id("postalCode").fill(zip_code)
        self.page.get_by_test_id("continue").click()

    def finish(self):
        self.page.get_by_test_id("finish").click()
        return self.page.locator(".complete-header")