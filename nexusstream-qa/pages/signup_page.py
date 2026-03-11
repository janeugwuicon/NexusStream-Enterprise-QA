from .base_page import BasePage


class SignupPage(BasePage):

    NAME = "[data-qa='signup-name']"
    EMAIL = "[data-qa='signup-email']"
    SIGNUP = "[data-qa='signup-button']"

    PASSWORD = "[data-qa='password']"
    FIRST = "[data-qa='first_name']"
    LAST = "[data-qa='last_name']"
    ADDRESS = "[data-qa='address']"
    STATE = "[data-qa='state']"
    CITY = "[data-qa='city']"
    ZIP = "[data-qa='zipcode']"
    MOBILE = "[data-qa='mobile_number']"

    CREATE = "[data-qa='create-account']"
    CONTINUE = "[data-qa='continue-button']"

    def create_account(self, name, email):

        self.fill(self.NAME, name)
        self.fill(self.EMAIL, email)
        self.click(self.SIGNUP)

        self.fill(self.PASSWORD, "Pass123!")
        self.fill(self.FIRST, name)
        self.fill(self.LAST, "User")
        self.fill(self.ADDRESS, "QA Street")
        self.fill(self.STATE, "CA")
        self.fill(self.CITY, "LA")
        self.fill(self.ZIP, "90001")
        self.fill(self.MOBILE, "123456789")

        self.click(self.CREATE)

    def continue_login(self):
        self.click(self.CONTINUE)