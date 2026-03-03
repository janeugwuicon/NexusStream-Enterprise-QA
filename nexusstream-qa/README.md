# NexusStream QA Automation

This folder contains the automation code and tests for the NexusStream QA project.

## What is this project?

- A simple QA automation project for a demo application called NexusStream.
- It shows how to write UI and API tests, run them, and create reports.
- The project is written in Python and uses Playwright and Pytest.

## Requirements

- Python 3.12 or newer
- `pip` for installing Python packages
- Playwright browsers (installed with `playwright install`)

## Setup (Windows)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

## Run tests

- Run all tests:

```powershell
pytest -v
```

- Run smoke tests only:

```powershell
pytest tests/smoke/ -q
```

## Project layout (short)

- `core/` - helpers and base page objects
- `pages/` - page objects
- `tests/` - test suites (ui, api, smoke)
- `data/` - test data
- `allure-results/` - test report output

## Contributing

- Please run tests locally before opening a PR.
- Keep commit messages short and meaningful.

Thanks for checking the NexusStream QA automation project.

