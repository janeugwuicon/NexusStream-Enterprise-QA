from core.base_page import BasePage

class CheckoutPage(BasePage):

    @property
    def success_header(self):
        return self.page.locator(".complete-header")

    @property
    def zip_code_input(self):
        return self.by_test_id("postalCode")

    def start_checkout(self):
        self.by_test_id("checkout").click()

    def fill_shipping(self, first: str, last: str, zip_code: str):
        self.by_test_id("firstName").fill(first)
        self.by_test_id("lastName").fill(last)
        self.zip_code_input.fill(zip_code)
        self.by_test_id("continue").click()

    def finish(self):
        self.by_test_id("finish").click()