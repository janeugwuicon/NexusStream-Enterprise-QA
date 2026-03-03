# 🚀 NexusStream: Enterprise Quality & AI Evaluation Framework

**A 16-week, production-grade QA portfolio project**  
**Status:** ✅ Month 1 Complete (Weeks 1–4 delivered); Month 2 in progress

[![Python Version](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://python.org)
[![Playwright](https://img.shields.io/badge/Playwright-Web%20Automation-2EAD33?logo=playwright)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing%20Framework-0A9EDC?logo=pytest)](https://docs.pytest.org/en/latest/)
[![K6](https://img.shields.io/badge/k6-Performance%20Testing-7D64FF?logo=k6)](https://k6.io/)
[![Postman](https://img.shields.io/badge/Postman-API%20Testing-FF6C37?logo=postman)](https://www.postman.com/)
[![Jira](https://img.shields.io/badge/Jira-Test%20Management-0052CC?logo=jira)](https://www.atlassian.com/software/jira)

---

## 📌 Executive Summary

**NexusStream** is a simulated E-commerce and Digital Content platform. This repository demonstrates a **complete quality engineering lifecycle** across 16 weeks, progressing from manual QA fundamentals → UI automation → performance testing → AI evaluation.

### 📊 Current Status: Month 1 ✅ COMPLETE

| Week | Topic | Status | Deliverables |
|------|-------|--------|--------------|
| **Week 1** | Manual Testing & Test Design | ✅ COMPLETE | 10 test cases, 6 defects identified |
| **Week 2** | bug Reporting & Triage | ✅ COMPLETE | 10 professional bug reports, triage process |
| **Week 3** | SQL & Database Validation | ✅ COMPLETE | SQL scripts, data integrity checks |
| **Week 4** | API Testing with Postman | ✅ COMPLETE | Postman collection, 15+ API tests |
| **Week 5** | Smoke Test Automation | 🔄 IN PROGRESS | Playwright scripts, CI workflow |

**Production Status:** ❌ NOT APPROVED — 2 critical blockers (payment, authentication)  
**Next Deadline:** Smoke automation (Week 5)

---

## 🛠️ Technology Stack

| Category | Tools |
|----------|-------|
| **Test Automation** | Playwright (UI), pytest (framework) |
| **API Testing** | Postman, Python requests |
| **Database** | PostgreSQL, SQL scripts |
| **Performance** | K6 (load testing) |
| **AI/LLM Quality** | DeepEval, Giskard |
| **CI/CD** | GitHub Actions, Allure Reports |
| **Agile** | Jira (test case, bug tracking) |
| **Patterns** | Page Object Model (POM), Data-Driven Testing (DDT) |

---

## 📂 Repository Structure

```
NexusStream-Enterprise-QA/
│
├── docs/                       # 📚 WEEKLY DELIVERABLES (organized by week)
│   ├── Week-01/               # ✅ Test strategy & cases (10 tests executed)
│   │   ├── Test-Strategy.md       (executed, 4 passed / 6 failed)
│   │   ├── Test-Cases.md          (all 10 cases with results)
│   │   └── README.md              (Week 1 summary)
│   │
│   ├── Week-02/               # ✅ Bug reports & triage (10 bugs filed)
│   │   ├── Test-Execution-Summary.md
│   │   ├── Sample-Bug-Reports.md  (5 production-quality examples)
│   │   ├── Bug-Triage-Process.md  (QA workflow)
│   │   └── README.md              (Week 2 summary)
│   │
│   ├── Week-03/               # 🔄 SQL validation (coming)
│   ├── Week-04/               # 🔄 Postman API testing (coming)
│   └── Week-05 to Week-16/    # Future months
│
├── tests/                      # 🧪 Python test suites (future)
│   ├── smoke/                  # Smoke tests (Month 2)
│   ├── ui/                     # Playwright UI tests (Month 2)
│   ├── api/                    # Python API tests (Month 3)
│   ├── integration/            # E2E tests (Month 3)
│   └── ai_eval/                # LLM evaluation (Month 4)
│
├── sql_scripts/                # SQL test scripts (Week 3)
├── performance/                # K6 load tests (Month 3)
├── data/                       # Test data (CSVs, JSON)
├── pages/                      # Page Object Model (Month 2)
├── .github/workflows/          # CI/CD pipelines (Month 2)
├── conftest.py                 # Pytest fixtures
├── pytest.ini                  # Pytest config
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🎯 Month 1 Deliverables (Complete)

### ✅ Week 1: Manual Testing & Test Design
**What:** Designed and executed 10 manual test cases covering login, shopping cart, and checkout flows.  
**Results:** 4 passed, 6 failed → 6 defects identified  
**Proof:** [docs/Week-01/](docs/Week-01/)

**Key Findings:**
- 🔴 **NXS-101:** Login email validation can be bypassed with whitespace (CRITICAL)
- 🔴 **NXS-102:** Failed payment still creates completed order (CRITICAL)
- 🟠 **NXS-103–106:** Additional issues in quantity validation, form validation, duplicate search results

### ✅ Week 2: Bug Reporting & Triage
**What:** Documented all defects professionally using Jira format; established bug triage process.  
**Deliverables:**
- 10 detailed bug reports with severity, impact, root cause
- Standardized triage workflow with roles and SLAs
- Production readiness assessment  
**Proof:** [docs/Week-02/](docs/Week-02/)

**What a Recruiter Sees:**
- ✅ You understand test execution and measurement
- ✅ You write professional bug reports
- ✅ You classify severity correctly (Critical vs. High vs. Medium)
- ✅ You identify root causes and business impact
- ✅ You establish repeatable QA processes

---

## ✅ Month 1 Weeks 3–4 (Completed)

### ✅ Week 3: SQL & Database Validation  
Executed a comprehensive suite of SQL queries to validate data integrity.  
**Deliverables:** Consolidated `validation_tests.sql`, database screenshots, README summary  
**Completion:** March 12, 2025

### ✅ Week 4: API Testing with Postman  
Created and executed a Postman collection covering core REST endpoints.  
**Deliverables:** Collection & environment exports, over 15 API assertions, documentation  
**Completion:** March 19, 2025

---

## 🔄 Month 2 Week 1 (In Progress)
Smoke tests written with Playwright and Python; CI workflow configured.  
Next: push smoke folder to GitHub and verify CI runs successfully.

---

## 📈 Full 16-Week Roadmap

| Month | Weeks | Focus | Outcome |
|-------|-------|-------|---------|
| **Month 1** | 1–4 | Manual Testing, Jira, SQL, Postman | **Junior QA Role Ready** |
| **Month 2** | 5–8 | Playwright UI Automation, Page Object Model, CI/CD | **Mid-Level SDET Ready** |
| **Month 3** | 9–12 | API Automation, End-to-End Tests, Performance (K6) | **Senior SDET Ready** |
| **Month 4** | 13–16 | AI/LLM Evaluation, Prompt Security, RAG Testing | **AI QA Expert** |

---

## 🚀 Quick Start

### For Recruiters & Hiring Managers
1. View **Month 1 deliverables** in the `docs/` folder
2. See **Week 1 test cases** and **Week 2 bug reports** for QA fundamentals
3. Check back for Weeks 3–4 (SQL and Postman testing)

### For Running the Tests (Once Weeks 3+ Complete)

```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run Smoke Tests (Month 2+)
pytest tests/smoke/ -v

# Run UI E2E Tests (Month 2+)
pytest tests/ui/ -m e2e

# Run API Tests (Month 3+)
pytest tests/api/ -v

# Generate Report
allure serve allure-results
```

## 🧪 QA Automation

The automation code and tests are in the `nexusstream-qa` folder. That folder has a simple README with setup and run instructions for beginners.

- To see automation details, open `nexusstream-qa/README.md`.
- Follow the steps there to set up a virtual environment, install dependencies, and run tests.


---

## 📊 Key Metrics (Month 1)

| Metric | Value |
|--------|-------|
| **Test Cases Planned** | 10 |
| **Test Cases Executed** | 10 (100%) |
| **Pass Rate** | 40% |
| **Defects Found** | 10 |
| **Critical Issues** | 2 |
| **Production Approved** | ❌ NO |
| **Timeline** | ✅ On schedule |

---

## 🔴 Production Blockers

### **NXS-101: Login Email Validation Bypass**
- **Severity:** CRITICAL
- **Issue:** Email validation doesn't trim whitespace; login succeeds with `user@example.com  ` (spaces)
- **Risk:** Account security, unauthorized access
- **Status:** Dev team assigned

### **NXS-102: Failed Payment Shows as Completed Order**
- **Severity:** CRITICAL
- **Issue:** Expired card payment fails (402) but order created with status="Completed"
- **Risk:** Inventory loss, revenue inaccuracy
- **Status:** Dev + Payment team assigned

> Both issues must be resolved before production sign-off.

---

## 👤 About This Portfolio

**Portfolio Owner:** Jane Ugwu  
**Framework:** NexusStream (16-week QA masterclass)  
**Purpose:** Demonstrate a complete quality engineering lifecycle from Junior → Senior → AI QA Expert  
**Audience:** Hiring managers, recruiters, tech leads  

Each week is designed to answer: *"What can you actually do as a QA engineer?"*

---

## 📞 Questions?

- **Week 1–2 Details:** See [docs/Week-01/](docs/Week-01/) and [docs/Week-02/](docs/Week-02/)
- **Test Cases:** [docs/Week-01/Test-Cases.md](docs/Week-01/Test-Cases.md)
- **Bug Reports:** [docs/Week-02/Sample-Bug-Reports.md](docs/Week-02/Sample-Bug-Reports.md)
- **Bug Triage Process:** [docs/Week-02/Bug-Triage-Process.md](docs/Week-02/Bug-Triage-Process.md)

---

**Last Updated:** March 5, 2025  
**Next Update:** Week 3 (SQL testing) by March 12, 2025
