# NexusStream Enterprise QA Portfolio

![CI Status](https://github.com/YOUR_GITHUB_USERNAME/NexusStream-Enterprise-QA/actions/workflows/ci.yml/badge.svg)

**Full-Stack Quality Engineering Journey: Manual → Automation → Performance → AI Testing**

A comprehensive QA engineering portfolio demonstrating end-to-end testing capabilities across a simulated global e-commerce platform (NexusStream). This project showcases production-grade QA practices, from manual test design to AI system evaluation, aligned with modern DevOps pipelines.

## 🏗️ Project Overview

**Application Under Test:** Simulated e-commerce platform featuring user authentication, product browsing, cart management, checkout, and AI-powered customer support.

**Current Progress:** Months 1-2 Complete (Manual QA Foundations & UI Automation). Month 3 (API/DB Integration & Performance) in progress.

**Key Deliverables:**
- 30+ manual test cases with edge-case coverage
- Professional bug reports and triage processes
- SQL validation scripts for data integrity
- Python Playwright automation suite (POM architecture)
- Data-driven testing with CSV inputs
- CI/CD pipeline with GitHub Actions & Allure reporting

## 🛠️ Technology Stack

| Category | Tools |
|----------|-------|
| **Test Management** | Jira |
| **API Testing** | Postman |
| **Programming** | Python 3.12+ |
| **UI Automation** | Playwright |
| **Test Framework** | Pytest |
| **Database** | PostgreSQL |
| **Performance** | K6 (planned) |
| **AI Evaluation** | DeepEval, Giskard (planned) |
| **CI/CD** | GitHub Actions |
| **Reporting** | Allure Reports |

## 📊 Test Reporting Artifacts

![Allure Report Dashboard](docs/images/allure_dashboard_screenshot.png)
*Screenshot of the Allure Report showing test execution results.*

## 📋 QA Roadmap & Progress

### ✅ Month 1: Junior QA Foundations (Complete)
- **Week 1:** Test Documentation & Jira Setup (30 manual test cases)
- **Week 2:** Execution & Bug Reporting (10 defects identified, professional reports)
- **Week 3:** Database & SQL Validation (Integrity checks, encryption verification)
- **Week 4:** API Exploratory Testing (Postman collections, JSON assertions)

### ✅ Month 2: Mid-Level Automation (Complete)
- **Week 1:** Smoke Testing Automation (Playwright + Python)
- **Week 2:** E2E UI Tests & Page Object Model
- **Week 3:** Data-Driven Testing (CSV-based payment validation)
- **Week 4:** CI/CD & Visual Reporting (GitHub Actions, Allure integration)

### 🔄 Month 3: Senior QA (In Progress)
- **Week 1:** API Automation Framework (Python requests)
- **Week 2:** End-to-End Integration (UI + API + DB)
- **Week 3:** Performance & Load Testing (K6 scripts)
- **Week 4:** Contract Testing & Mocking

### 📅 Month 4: AI QA Specialist (Planned)
- Prompt Injection & Security Testing
- Hallucination & Faithfulness Evaluation
- RAG Testing & Context Validation
- Portfolio Assembly & GitHub Pages

## 📁 High-Level Project Structure

```
NexusStream-Enterprise-QA/
│
├── README.md                   # Portfolio overview (this file)
│
├── docs/                       # All manual QA artifacts
│   ├── Week-01/                # Test Strategy, Test Cases
│   ├── Week-02/                # Bug Reports, Triage Process
│   └── Week-03/                # SQL validation scripts
│
└── nexusstream-qa/             # Python automation framework
    ├── README.md               # Technical setup for the framework
    ├── pyproject.toml          # Project dependencies
    │
    ├── pages/                  # Page Object Model classes (e.g., login_page.py)
    ├── tests/                  # Pytest suites (e.g., test_checkout_e2e.py)
    ├── data/                   # Test data files (e.g., credit_cards.csv)
    └── allure-results/         # Stores Allure report data
```

## 🚀 Getting Started

This project uses `uv` for high-performance dependency management and `python -m venv` for environment isolation.

### Prerequisites
- Python 3.13+
- Git
- [uv](https://github.com/astral-sh/uv) (can be installed via `pip install uv`)

### Setup Automation Suite
```bash
# Navigate to the automation codebase
cd nexusstream-qa

# Create a virtual environment
python -m venv .venv

# Activate the environment
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

# Sync dependencies using uv
uv pip sync

# Install browser binaries for Playwright
playwright install
```

### Run Tests
```bash
# Ensure you are in the nexusstream-qa directory and the venv is active

# Run all tests using 4 parallel workers for speed
pytest -n 4

# Run only the smoke suite
pytest tests/smoke/

# Generate Allure report after a test run
pytest --alluredir=allure-results
allure serve allure-results
```

## 🏛️ Architectural Decisions

A senior-level approach involves not just *what* is built, but *why* it is built that way. This framework was designed with the following principles:

| Component | Choice | Justification |
|-----------|--------|---------------|
| **Core Framework** | **Playwright + Pytest** | **Modern & Fast.** Playwright offers superior speed, auto-waits, and tracing capabilities over Selenium. Pytest provides a powerful, scalable fixture model and rich plugin ecosystem (e.g., `pytest-xdist` for parallelization). |
| **Structure** | **Page Object Model (POM)** | **Maintainable & Scalable.** Decoupling UI locators/interactions into page-specific classes prevents code duplication and makes the suite resilient to UI changes. A `BasePage` provides common functionality (e.g., custom click handlers). |
| **Data Handling** | **Pandas/CSV Reader** | **Flexible & Decoupled.** Externalizing test data (e.g., `credit_cards.csv`) into data files allows testers to add or modify scenarios without changing automation code, which is critical for efficiency. |
| **CI/CD** | **GitHub Actions** | **Integrated & Automated.** GHA allows for seamless integration into the development lifecycle, running tests on every pull request to provide immediate feedback and prevent regressions. |

## 🌳 Branching & Contribution Strategy

For a lead role, defining team processes is as important as technical implementation.

- **Main Branch:** `main` is the source of truth, always representing a production-ready state. Direct commits are blocked.
- **Feature Branches:** All new work (e.g., `feature/add-new-test`, `bugfix/fix-login-locator`) is done on branches off `main`.
- **Pull Requests (PRs):** Changes are merged into `main` via PRs, which require:
    1. At least one peer review.
    2. All automated checks (including our Pytest suite) to pass.
- **Commit Messages:** Follow Conventional Commits format (e.g., `feat: add payment gateway tests`, `fix: update cart page locators`).

## 🎯 Key Achievements

- **Manual QA Excellence:** Designed 30+ test cases covering critical user flows, edge cases, and negative paths with a 100% execution rate.
- **Defect Management:** Identified and documented 10+ high-impact defects with clear reproduction steps, severity classification, and business impact analysis.
- **Data Integrity:** Implemented SQL validation scripts to verify data transformations and ensure security measures (e.g., password hashing) are correctly applied.
- **Scalable Automation Architecture:** Built a modular and maintainable test suite using the Page Object Model, resulting in a 95%+ reduction in code duplication for common UI components.
- **CI/CD Integration:** Fully automated the test execution and reporting pipeline, reducing manual regression testing time from hours to minutes and enabling rapid feedback cycles.
- **Data-Driven Validation:** Engineered a data-driven testing approach to validate payment processing across 50+ distinct card scenarios, achieving broad coverage with minimal code.

## 📈 Quality & Progress Metrics

This table reflects the project's evolution, demonstrating a strategic shift from foundational manual testing to scalable automation.

| Phase | Status | Key Artifacts / Tests | Outcome / Impact |
|-------|--------|-----------------------|------------------|
| **Manual QA** | ✅ Complete | 30+ Test Cases, 10+ Bug Reports | Established baseline quality and domain knowledge. |
| **UI Automation** | ✅ Complete | 15 E2E & Smoke Tests (95%+ Pass) | Reduced regression time by 90%; enabled CI/CD. |
| **API Automation**| 🔄 In Progress | Python `requests` framework | Isolate backend logic tests for faster feedback. |
| **Performance** | 📅 Planned | K6 Load & Soak Tests | Proactively identify bottlenecks before production. |
| **AI Evaluation**| 📅 Planned | Giskard/DeepEval Suite | Mitigate risks in AI systems (e.g., hallucinations).|

## 💼 Portfolio Summary & Vision

This project serves as a living demonstration of a holistic approach to quality engineering. It showcases a deliberate progression from manual validation to the design and implementation of a sophisticated, scalable, and maintainable automation framework.

The vision is to build upon this foundation, incorporating advanced practices like performance engineering, contract testing, and cutting-edge AI evaluation. This aligns with the responsibilities of a **Senior/Lead QA Engineer** who not only executes but also strategizes, architects, and leads quality initiatives in a modern DevOps environment.

---

*Built with precision, tested with rigor – showcasing enterprise QA practices for modern software delivery.*