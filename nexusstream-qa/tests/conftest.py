import pytest
from playwright.sync_api import Playwright


# -----------------------------------
# Global selector configuration
# -----------------------------------
@pytest.fixture(scope="session", autouse=True)
def configure_selectors(playwright: Playwright):
    """
    Standardize test id selector across framework.
    SauceDemo uses data-test attribute.
    """
    playwright.selectors.set_test_id_attribute("data-test")