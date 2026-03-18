# Week 3: Database & SQL Validation Testing

**Phase:** Month 3 – Senior QA (Backend & Data Integrity)
**Focus:** Verifying application data at the source.
**Completed:** February 27, 2026  

---

## Overview

This phase demonstrates the ability to bypass the UI and test the application's backend directly. By querying the database, we can validate data integrity, referential consistency, and business logic that is impossible to see from the frontend alone. All tests were performed against a PostgreSQL database.

## Validation Areas

The SQL validation script (`validation_tests.sql`) covers five critical domains:

| Area | Focus | Key Validation Technique |
|---|---|---|
| **User Registration** | Passwords are not stored in plain text. | `SELECT` query on the `users` table to check the password hash format. |
| **Order Creation** | Orders correctly link to users and products. | `JOIN` between `orders`, `users`, and `order_items` to verify foreign key relationships. |
| **Inventory Management**| Stock levels decrease accurately after an order. | Comparing `products.stock_quantity` before and after a simulated order. |
| **Payment State** | Order status is correctly synchronized with payment. | `SELECT` on `orders` to ensure `status` is 'COMPLETED' only when a transaction ID is present. |
| **Refund Logic** | Inventory is correctly restocked on a refund. | Validating that a 'REFUNDED' order status triggers an increment in `products.stock_quantity`. |

## Summary of Results

- **All 5 validation areas passed** with no data integrity issues found.
- **Referential integrity** between `users`, `products`, and `orders` is correctly maintained.
- **Security check** confirmed that passwords are hashed.

## Why This Matters for a Senior Role

This work proves capabilities that are essential for a senior position:

- **Thinking Beyond the UI:** Understanding that the user interface is only one layer of the application.
- **Writing & Interpreting SQL:** Ability to write `SELECT` statements with `JOINs` and aggregates to find complex data issues.
- **Backend Defect Detection:** The skill to identify bugs (e.g., inventory not updating) that would be missed by UI-only testing.
- **Enterprise-Level Practices:** Applying data-layer validation is a hallmark of a mature, enterprise-grade quality process.

---

*This deliverable is ready for a hiring manager to review as clear evidence of backend testing and SQL proficiency.*
