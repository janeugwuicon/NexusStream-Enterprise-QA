import os
import pytest
from playwright.sync_api import Playwright
from core.config import HEADLESS
from pages.login_page import LoginPage

@pytest.fixture(scope="session", autouse=True)
def configure_selectors(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture(scope="session")
def auth_state(playwright: Playwright):
    os.makedirs(".auth", exist_ok=True)
    state_path = ".auth/state.json"

    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()
    page = context.new_page()

    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")

    context.storage_state(path=state_path)
    browser.close()
    return state_path

@pytest.fixture
def auth_page(browser, auth_state):
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    yield page
    context.close()