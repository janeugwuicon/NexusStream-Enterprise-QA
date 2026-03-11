# NexusStream QA Automation Portfolio

This repository contains the automation code and supporting documentation for the NexusStream QA project, designed to showcase a comprehensive range of quality assurance skills.

## What is this project?

This is a portfolio project that demonstrates a full-spectrum QA process, from manual test planning to automated backend validation.

- **Automation Framework**: A UI test automation framework built with Python, Playwright, and Pytest.
- **Test Application**: All tests are run against [Automation Exercise](https://automationexercise.com/).
- **Methodologies**: The framework uses the Page Object Model (POM) for maintainability and demonstrates smoke, end-to-end, and data-driven testing patterns.
- **Comprehensive Documentation**: The `/docs` directory contains detailed artifacts from manual testing phases, including test strategies, bug reports, triage processes, and SQL validation scripts, providing context for the automation suite.
- **Reporting**: Generates detailed Allure reports for visualizing test results.

## Requirements

- Python 3.13 or newer
- `uv` for dependency management (modern Python package manager)
- Playwright browsers

## Setup

1. Install `uv` if not already installed:
   ```sh
   # On Windows
   winget install astral-sh.uv

   # Or using pip
   pip install uv
   ```

2. Install dependencies using uv:
   ```sh
   uv sync
   ```

3. Install Playwright browsers:
   ```sh
   uv run playwright install
   ```

## Run tests

Run all tests:
```sh
uv run pytest
```

Run smoke tests only:
```sh
uv run pytest tests/smoke/
```

Run with Allure reporting:
```sh
uv run pytest --alluredir=allure-results
allure serve allure-results
```

## Project Structure

- `pages/` - Page Object Model classes for different pages
- `tests/` - Test suites organized by type (smoke, e2e, ddt)
- `utils/` - Utility functions (e.g., CSV data reader)
- `data/` - Test data files
- `allure-results/` - Generated test reports

## Test Types

- **Smoke Tests**: Basic functionality verification (login, homepage load)
- **E2E Tests**: Complete user journey testing (login → add to cart → checkout → order completion)
- **DDT (Data-Driven Tests)**: Parameterized tests with CSV data (payment gateway validation)

## CI/CD

GitHub Actions workflow runs tests on every push.

## Contributing

- Please run tests locally before opening a PR.
- Keep commit messages short and meaningful.

Thanks for checking the NexusStream QA automation project.
