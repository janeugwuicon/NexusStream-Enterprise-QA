from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def load(self):
        self.visit("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.fill(self.username, user)
        self.fill(self.password, pwd)
        self.click(self.login_btn)