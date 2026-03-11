from .base_page import BasePage


class LoginPage(BasePage):

    EMAIL = "[data-qa='login-email']"
    PASSWORD = "[data-qa='login-password']"
    LOGIN = "[data-qa='login-button']"
    USER = "li:has-text('Logged in as') b"

    def login(self, email, password):
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN)