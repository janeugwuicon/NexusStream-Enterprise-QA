from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_btn = self.page.locator("#checkout")
        self.first_name = self.page.locator("#first-name")
        self.last_name = self.page.locator("#last-name")
        self.postal = self.page.locator("#postal-code")
        self.continue_btn = self.page.locator("#continue")
        self.finish_btn = self.page.locator("#finish")
        self.success = self.page.locator(".complete-header")
        self.error = self.page.locator("[data-test='error']")

    def fill_details(self, f_name, l_name, zip_code):
        self.first_name.fill(f_name)
        self.last_name.fill(l_name)
        self.postal.fill(zip_code)
        self.continue_btn.click()

    def finish(self):
        self.finish_btn.click()