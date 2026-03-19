from pages.base_page import BasePage
class HomePage(BasePage):
    def __init__(self, page):
        self.page = page
        self.logo = page.locator(".login_logo")

    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def is_loaded(self):
        return self.logo.is_visible()