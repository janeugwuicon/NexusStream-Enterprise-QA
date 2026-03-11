from playwright.sync_api import Page

BASE_URL = "https://automationexercise.com"


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = ""):
        self.page.goto(f"{BASE_URL}{path}")

    def click(self, locator: str):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.click()

    def fill(self, locator: str, value: str):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.fill(value)

    def type(self, locator: str, value: str):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.type(value)

    def visible(self, locator: str):
        return self.page.locator(locator).is_visible()