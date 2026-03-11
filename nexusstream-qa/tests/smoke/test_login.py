import uuid
from playwright.sync_api import expect


def test_login(page, signup, login):

    email = f"user_{uuid.uuid4().hex[:6]}@test.com"

    signup.open("/login")
    signup.create_account("Jane", email)
    signup.continue_login()

    page.locator("a[href='/logout']").click()

    signup.open("/login")
    login.login(email, "Pass123!")

    expect(page.locator(login.USER)).to_have_text("Jane")