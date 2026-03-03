def test_api_health(playwright):
    request = playwright.request.new_context()
    response = request.get("https://www.saucedemo.com")
    assert response.status == 200