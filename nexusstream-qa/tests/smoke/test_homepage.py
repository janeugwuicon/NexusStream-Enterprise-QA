import pytest

@pytest.mark.smoke
def test_homepage_load(page):
    page.goto("/")
    assert page.title() != ""