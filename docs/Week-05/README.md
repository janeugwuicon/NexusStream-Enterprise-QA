# Week 5: Smoke Test Automation with Playwright (Month 2 – Week 1)

**Phase:** Mid‑Level QA / SDET – UI Test Automation & Frameworks  
**Target Dates:** March 20–26, 2025  
**Estimated Effort:** 8–10 hours

---

## 🎯 Objective

Move from manual clicking to code-driven browser automation using **Python** and **Playwright**. Build a small smoke test suite for a demo e‑commerce site and run it automatically via GitHub Actions. This week lays the foundation for genuine automation work expected in mid‑level QA roles.

---

## 📋 Week 1 Deliverables

1. **Python test scripts** using Pytest & Playwright
   - `tests/smoke/test_smoke.py` – verifies valid credentials reach the dashboard and homepage elements
   - `tests/e2e/test_checkout_e2e.py` – end-to-end purchase flow using the local demo site
   - Page Object Model classes in `pages/` encapsulate locators and actions for login, inventory, cart and checkout
   - A small static website under `demo_site/` lets you run the tests without hitting an external service

> **Note:** the original training materials pinned `pytest` very tightly, which now
> conflicts with newer `pytest-playwright` releases. the repo’s `requirements.txt`
> has been relaxed to `pytest>=8,<10` and `pytest-playwright>=0.7.2` so you can run
> `pip install -r requirements.txt` without dependency errors.
   - Page Object Model classes in `tests/smoke/pages/` to encapsulate locators and actions

### 🛠 Setup Instructions

1. Create/activate a Python environment (venv/conda/etc.).
2. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Install the browser driver via Playwright:

   ```bash
   python -m playwright install chromium --with-deps
   ```

4. Provide credentials either via `.env` or environment variables:

   ```bash
   export TEST_USERNAME=standard_user
   export TEST_PASSWORD=secret_sauce
   ```

5. Finally run the tests with `pytest` from the project root.
2. **Requirements file** (`requirements.txt`) listing `pytest` and `playwright`
3. **CI workflow** – GitHub Action (`.github/workflows/playwright.yml`) that installs dependencies, runs `playwright install`, and executes the smoke tests on each push/PR
4. **Clean project structure** with `tests/` packages and POM files

---

## 🧰 Technologies & Concepts Covered

- **Playwright for Python** – browser automation library supporting Chromium, Firefox, WebKit
- **Pytest** – test runner with fixtures for setup/teardown
- **Page Object Model (POM)** – maintainable design pattern separating page details from test logic
- **GitHub Actions** – simple CI/CD pipeline to run tests on push/PR
- **Python fundamentals** – functions, classes, fixtures, imports

---

## 🔗 Example Code Snippet

```python
# login_page.py (POM)
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def goto(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
```

---

## 📈 Why Recruiters Should Care

- ✅ You automate UI workflows, not just click manually
- ✅ You apply Python to real‑world testing problems
- ✅ You design maintainable test code (POM) for scalability
- ✅ You integrate tests into a CI pipeline (GitHub Actions)
- ✅ You can walk into a team and immediately contribute to automation efforts

---

## 📝 Notes

- Tests use [SauceDemo](https://www.saucedemo.com) as a stable demo site with known selectors and credentials (`standard_user` / `secret_sauce`).
- Headless browser is used in CI but you can set `headless=False` locally to watch the execution.
- To run locally:
  ```sh
  pip install -r requirements.txt
  playwright install
  pytest tests/smoke
  ```

---

*Status: 🔄 NOT STARTED – scripts written; ready for execution and push to GitHub.*