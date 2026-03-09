# NexusStream Enterprise QA Portfolio

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

## 📁 Project Structure

```
NexusStream-Enterprise-QA/
│
├── README.md                           # This file
│
├── docs/                               # Manual QA Documentation
│   ├── Week-01/                        # Test Planning & Cases
│   │   ├── README.md
│   │   ├── Test-Cases.md
│   │   └── Test-Strategy.md
│   ├── Week-02/                        # Bug Reporting & Triage
│   │   ├── README.md
│   │   ├── Bug-Triage-Process.md
│   │   ├── Sample-Bug-Reports.md
│   │   ├── Test-Execution-Summary.md
│   │   └── Bug-screenshots/
│   └── Week-03/                        # Database Validation
│       ├── README.md
│       ├── validation_tests.sql
│       └── DB-Screenshots/
│
└── nexusstream-qa/                     # Automation Codebase
    ├── README.md                       # Setup & Run Instructions
    ├── pyproject.toml                  # Dependencies
    ├── pytest.ini                      # Test Configuration
    ├── main.py                         # Entry Point
    │
    ├── pages/                          # Page Object Models
    │   ├── login_page.py
    │   ├── inventory_page.py
    │   ├── cart_page.py
    │   ├── checkout_page.py
    │   └── payment_page.py
    │
    ├── tests/                          # Test Suites
    │   ├── smoke/                      # Health Checks
    │   │   ├── test_login_smoke.py
    │   │   └── test_homepage.py
    │   ├── e2e/                        # End-to-End Flows
    │   │   └── test_checkout_e2e.py
    │   └── ddt/                        # Data-Driven Tests
    │       └── test_payment_gateways.py
    │
    ├── data/                           # Test Data
    │   └── credit_cards.csv
    │
    └── allure-results/                 # Test Reports
```

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Git
- Virtual Environment (venv)

### Setup Automation Suite
```bash
cd nexusstream-qa
python -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
playwright install
```

### Run Tests
```bash
# All tests
pytest -v

# Smoke tests only
pytest tests/smoke/ -q

# With Allure reporting
pytest --alluredir=allure-results
allure serve allure-results
```

## 🎯 Key Achievements

- **Manual QA Excellence:** Designed 30+ test cases covering critical user flows with 100% execution rate
- **Defect Management:** Identified and documented 10+ defects with proper severity classification and business impact analysis
- **Database Proficiency:** Implemented SQL validation scripts ensuring data integrity and security
- **Automation Architecture:** Built maintainable test suite using Page Object Model with 95%+ code reusability
- **CI/CD Integration:** Automated test execution with visual reporting and failure notifications
- **Data-Driven Testing:** Validated payment processing across 50+ card scenarios using CSV-driven approach

## 📈 Quality Metrics

| Phase | Test Cases | Pass Rate | Defects Found | Automation Coverage |
|-------|------------|-----------|---------------|---------------------|
| Manual QA | 30 | 40% | 10 | 0% |
| UI Automation | 15 | 87% | 2 | 100% |
| API Testing | Planned | - | - | - |
| Performance | Planned | - | - | - |

## 👨‍💻 About the QA Engineer

This portfolio demonstrates expertise in:
- **Test Strategy & Planning** (Requirements analysis, risk assessment)
- **Manual Testing** (Edge-case identification, defect reporting)
- **Automation Engineering** (Python, Playwright, Pytest)
- **Database Testing** (SQL validation, data integrity)
- **CI/CD Integration** (GitHub Actions, reporting)
- **Performance Testing** (Load simulation, metrics analysis)
- **AI System Evaluation** (Security, hallucination detection)

**Goal:** Transition to Senior QA Engineer role with focus on test automation, performance engineering, and AI quality assurance.

---

*Built with precision, tested with rigor – showcasing enterprise QA practices for modern software delivery.*