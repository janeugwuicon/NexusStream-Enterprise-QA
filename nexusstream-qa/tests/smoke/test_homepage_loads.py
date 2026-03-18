from pages.home_page import HomePage

def test_homepage_load(page):
    home = HomePage(page)
    home.load()

    assert home.is_loaded()