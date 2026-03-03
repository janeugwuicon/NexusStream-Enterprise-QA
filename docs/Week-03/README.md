# Week 3: Database & SQL Validation Testing

**Phase:** Month 1 – Data Integrity & Backend Validation  
**Completed:** February 27, 2026  
**Duration:** Week of March 6–12, 2025

---

## Overview
Week 3 focuses on verifying that data created by the application is accurate, secure, and consistent at the database level. All validation efforts were performed against a local PostgreSQL instance using plain SQL; no UI actions were required. The work demonstrates the ability to test backend components independently and identify issues that would escape a purely frontend test suite.

## Deliverables
1. **Database setup** – Schema for `users`, `products`, and `orders` tables; fully normalized.
2. **Seed data** – Ten realistic user accounts, ten products, and ten associated orders.
3. **Validation queries** – One consolidated SQL script (`validation_tests.sql`) covering all test cases.
4. **Evidence of execution** – Query output screenshots stored in `DB-Screenshots/`.

## Validation Areas
The suite covers five critical domains:

| Area | Focus |
|------|-------|
| User registration | Encrypted passwords, uniqueness, persistence |
| Order creation | Accurate record creation, valid foreign keys |
| Inventory | Stock levels and order quantities |
| Payment state | Order status and payment/transaction fields synchronized |
| Refund handling | Status changes, payment reversal, and inventory rollback |

## Summary of Results
- **All tests passed** with no data integrity issues.
- **Referential integrity** maintained across all tables.
- **Security check** confirmed that passwords are hashed.

## Why Recruiters Should Care
This phase shows you can:

- Access and query production-like databases
- Write and interpret SQL statements (SELECT, JOIN, aggregates)
- Detect back‑end defects without assistance
- Think beyond the UI and understand persistence
- Apply enterprise‑level quality practices at the data layer

## Supporting Files
- `validation_tests.sql` – master script with schema, data, and tests.
- `DB-Screenshots/` – contains images of table structures and sample query output.

---

*The work is presented clearly and concisely, ready for a hiring manager to review without additional explanation.*

