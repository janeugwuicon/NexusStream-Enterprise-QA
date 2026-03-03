from playwright.sync_api import Page
from core.logger import logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def by_test_id(self, value: str):
        return self.page.get_by_test_id(value)