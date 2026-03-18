from pages.login_page import LoginPage

def test_valid_login(page):
    lp = LoginPage(page)
    lp.load()
    lp.login("standard_user", "secret_sauce")

    assert "inventory" in page.url


def test_invalid_login(page):
    lp = LoginPage(page)
    lp.load()
    lp.login("wrong_user", "wrong_pass")

    assert lp.error.is_visible()


def test_locked_user_negative(page):
    lp = LoginPage(page)
    lp.load()
    lp.login("locked_out_user", "secret_sauce")

    assert "locked out" in lp.error.inner_text().lower()