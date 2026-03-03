from core.base_page import BasePage
from core.config import BASE_URL

class LoginPage(BasePage):

    def load(self):
        self.navigate(BASE_URL)

    def login(self, username: str, password: str):
        self.by_test_id("username").fill(username)
        self.by_test_id("password").fill(password)
        self.by_test_id("login-button").click()