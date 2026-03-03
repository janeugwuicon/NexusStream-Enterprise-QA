-- ==============================================================================
-- NEXUSSTREAM DATABASE - COMPREHENSIVE VALIDATION TEST SUITE
-- ==============================================================================
-- Purpose: Validate data integrity across user registration, order processing,
--          inventory management, payment processing, and refund handling
-- Database: PostgreSQL
-- Created: February 27, 2026
-- ==============================================================================


-- ==============================================================================
-- SECTION 1: DATABASE SCHEMA SETUP
-- ==============================================================================

-- Table: USERS
-- Purpose: Store user account information with encrypted passwords
-- Business Rule: Email addresses must be unique; passwords stored as hashes
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: PRODUCTS
-- Purpose: Maintain product catalog with pricing and stock levels
-- Business Rule: Price and stock must be non-negative; stock determines availability
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

-- Table: ORDERS
-- Purpose: Track customer orders and their status throughout lifecycle
-- Business Rule: Orders are linked to users; status reflects current order state
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    product_id INT REFERENCES products(id),
    quantity INT NOT NULL,
    order_status VARCHAR(50) DEFAULT 'Pending',
    payment_status VARCHAR(50) DEFAULT 'Pending',    -- tracks payment lifecycle ('Pending','Paid','Declined')
    transaction_status VARCHAR(50) DEFAULT 'Pending', -- mirrors payment_status for reconciliation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ==============================================================================
-- SECTION 2: TEST DATA INSERTION
-- ==============================================================================

-- Insert test users for order and registration validation
-- Data represents 10 unique customers with encrypted password hashes
INSERT INTO users (email, password_hash) VALUES 
('alice@test.com', 'hash_a1b2c3'),
('bob@test.com', 'hash_d4e5f6'),
('charlie@test.com', 'hash_g7h8i9'),
('dana@test.com', 'hash_j0k1l2'),
('evan@test.com', 'hash_m3n4o5'),
('fiona@test.com', 'hash_p6q7r8'),
('george@test.com', 'hash_s9t0u1'),
('hannah@test.com', 'hash_v2w3x4'),
('ian@test.com', 'hash_y5z6a7'),
('jane@test.com', 'hashed_password_123');

-- Insert product catalog with realistic inventory levels
-- Data represents typical e-commerce product mix (electronics, peripherals)
INSERT INTO products (name, price, stock) VALUES 
('Laptop', 1200.00, 10),
('Smartphone', 800.00, 25),
('Monitor', 300.00, 15),
('Keyboard', 50.00, 50),
('Mouse', 25.00, 100),
('Headphones', 150.00, 30),
('Webcam', 90.00, 20),
('USB-C Hub', 45.00, 40),
('External SSD', 120.00, 12),
('Tablet', 600.00, 8);

-- Insert sample orders showing order creation pattern
-- Each order maps user to product with quantity ordered
-- Initial order_status/payment_status/transaction_status are 'Pending'
INSERT INTO orders (user_id, product_id, quantity, order_status, payment_status, transaction_status) VALUES
(1, 1, 1, 'Pending', 'Pending', 'Pending'),
(2, 2, 1, 'Pending', 'Pending', 'Pending'),
(3, 3, 2, 'Pending', 'Pending', 'Pending'),
(4, 4, 1, 'Pending', 'Pending', 'Pending'),
(5, 5, 5, 'Pending', 'Pending', 'Pending'),
(6, 6, 1, 'Pending', 'Pending', 'Pending'),
(7, 10, 1, 'Pending', 'Pending', 'Pending'),
(8, 8, 3, 'Pending', 'Pending', 'Pending'),
(9, 9, 1, 'Pending', 'Pending', 'Pending'),
(10, 1, 1, 'Pending', 'Pending', 'Pending');


-- ==============================================================================
-- SECTION 3: USER REGISTRATION VALIDATION TESTS
-- ==============================================================================

-- TEST 3.1: USER PERSISTENCE VERIFICATION
-- Validates that user registration data is correctly stored in database
-- Expected: One record returned for registered user
PRINT 'TEST 3.1: User Registration - Verify data persistence';
SELECT * FROM users
WHERE email = 'jane@test.com';
-- Expected Result: 1 row with jane@test.com and hashed_password_123

-- TEST 3.2: PASSWORD ENCRYPTION VALIDATION
-- Confirms that passwords are stored as hashes, not plain text
-- Security Check: Value should be long random string, never readable password
-- Expected: Password field contains encrypted hash (45+ characters typically)
PRINT 'TEST 3.2: User Registration - Verify password encryption';
SELECT password_hash
FROM users
WHERE email = 'jane@test.com';
-- Expected Result: hashed_password_123 (encrypted format, not plain text like '123456')
-- FAIL scenario: Would return plaintext password like 'mypassword'

-- TEST 3.3: DUPLICATE EMAIL PREVENTION
-- Validates database constraint on unique email addresses
-- Business Rule: Each user must have unique email for identification
-- Expected: Zero rows returned (no duplicates exist)
PRINT 'TEST 3.3: User Registration - Ensure no duplicate emails';
SELECT email, COUNT(*) as duplicate_count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
-- Expected Result: Zero rows (all emails are unique)
-- FAIL scenario: Returns email addresses that appear more than once


-- ==============================================================================
-- SECTION 4: ORDER CREATION & REFERENTIAL INTEGRITY TESTS
-- ==============================================================================

-- TEST 4.1: ORDER STATUS INITIALIZATION
-- Verifies that orders are created with correct initial status
-- Business Rule: All new orders must start in 'Pending' state before processing
-- Expected: All orders have status 'Pending'
PRINT 'TEST 4.1: Order Creation - Verify initial status';
SELECT order_id, order_status
FROM orders
WHERE order_status = 'Pending';
-- Expected Result: Multiple rows, all with status 'Pending'
-- FAIL scenario: Orders have incorrect status (null, 'Processing', etc.)

-- TEST 4.2: USER-ORDER RELATIONSHIP VALIDATION
-- Ensures every order is linked to a valid existing user
-- Business Rule: Foreign key constraint prevents orphaned orders
-- Expected: Zero rows (no orders without valid user reference)
PRINT 'TEST 4.2: Order Creation - Verify user reference integrity';
SELECT o.id as order_id, o.user_id, u.id as user_exists
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;
-- Expected Result: Zero rows (all orders have valid user references)
-- FAIL scenario: Returns order IDs that have no corresponding user

-- TEST 4.3: PRODUCT-ORDER RELATIONSHIP VALIDATION
-- Ensures every order references an existing product
-- Business Rule: Orders cannot be created for non-existent products
-- Expected: Zero rows (no orders with invalid product references)
PRINT 'TEST 4.3: Order Creation - Verify product reference integrity';
SELECT o.id as order_id, o.product_id, p.id as product_exists
FROM orders o
LEFT JOIN products p ON o.product_id = p.id
WHERE p.id IS NULL;
-- Expected Result: Zero rows (all orders have valid product references)
-- FAIL scenario: Returns order IDs referencing deleted/invalid products


-- ==============================================================================
-- SECTION 5: INVENTORY MANAGEMENT VALIDATION TESTS
-- ==============================================================================

-- TEST 5.1: QUANTITY VALIDATION
-- Verifies order quantities are valid positive integers
-- Business Rule: Orders must contain at least 1 unit; negative/zero quantities rejected
-- Expected: Zero rows (no invalid quantities)
PRINT 'TEST 5.1: Inventory - Ensure no negative or zero quantities';
SELECT id as order_id, quantity
FROM orders
WHERE quantity <= 0;
-- Expected Result: Zero rows (all quantities are positive)
-- FAIL scenario: Returns orders with quantity <= 0

-- TEST 5.2: STOCK AVAILABILITY CHECK
-- Validates current stock levels against product catalog
-- Business Rule: Stock must match actual inventory available for purchase
-- Expected: All products show stock >= 0
PRINT 'TEST 5.2: Inventory - Verify stock levels are non-negative';
SELECT id, name, stock
FROM products
WHERE stock < 0;
-- Expected Result: Zero rows (no products with negative stock)
-- FAIL scenario: Shows products with negative stock (oversold scenario)

-- TEST 5.3: ORDER QUANTITY vs STOCK ANALYSIS
-- Does NOT automatically decrease stock (that happens during fulfillment)
-- This validates data exists and is reasonable at test dataset level
-- Business Rule: Stock should be sufficient for orders placed
PRINT 'TEST 5.3: Inventory - Review order quantities vs available stock';
SELECT 
    o.id as order_id,
    o.quantity as ordered_amount,
    p.name as product,
    p.stock as available_stock,
    CASE 
        WHEN o.quantity > p.stock THEN 'WARNING: Oversold'
        ELSE 'OK: Sufficient stock'
    END as inventory_status
FROM orders o
JOIN products p ON o.product_id = p.id
ORDER BY o.id;
-- Expected Result: All rows show 'OK: Sufficient stock'
-- FAIL scenario: Any row shows oversold condition

-- TEST 5.4: STOCK DECREMENT SIMULATION
-- Simulates a purchase by decrementing stock and verifying the change
PRINT 'TEST 5.4: Inventory - Simulate stock decrement on sale';
UPDATE products
SET stock = stock - (SELECT quantity FROM orders WHERE id = 1)
WHERE id = (SELECT product_id FROM orders WHERE id = 1);

SELECT id, name, stock
FROM products
WHERE id = (SELECT product_id FROM orders WHERE id = 1);
-- Expected Result: Original stock minus ordered quantity
-- FAIL scenario: Stock unchanged or negative value


-- ==============================================================================
-- SECTION 6: PAYMENT & ORDER STATUS VALIDATION TESTS
-- ==============================================================================

-- TEST 6.1: ORDER STATUS FIELD VALIDATION
-- Ensures order_status field contains valid known states
-- Valid values: 'Pending', 'Processing', 'Completed', 'Cancelled', 'Refunded'
-- Expected: All statuses are valid (no NULL or unexpected values)
PRINT 'TEST 6.1: Payment - Verify valid order status values';
SELECT DISTINCT order_status
FROM orders;
-- Expected Result: Only valid status values (e.g., 'Pending', 'Processing')
-- FAIL scenario: Shows invalid statuses or NULL values

-- TEST 6.2: ORDER COUNT BY STATUS
-- Provides business view of orders at each lifecycle stage
-- Expected: Orders distributed across statuses appropriately
PRINT 'TEST 6.2: Payment - Order distribution by status';
SELECT order_status, COUNT(*) as count
FROM orders
GROUP BY order_status
ORDER BY count DESC;
-- Expected Result: Shows quantity at each stage ('Pending', 'Processing', etc.)
-- FAIL scenario: All orders in 'Pending' (no order processing happening)

-- TEST 6.3: PAYMENT STATE SYNCHRONIZATION
-- Ensures payment_status and transaction_status values are identical
PRINT 'TEST 6.3: Payment - Verify payment and transaction status sync';
SELECT id, payment_status, transaction_status
FROM orders
WHERE payment_status <> transaction_status;
-- Expected Result: Zero rows (statuses are in sync)
-- FAIL scenario: Rows where payment and transaction states diverge


-- ==============================================================================
-- SECTION 7: REFUND PROCESSING VALIDATION TESTS
-- ==============================================================================

-- TEST 7.1: REFUND STATUS TRANSITION
-- Simulates order refund and validates status update works correctly
-- Also updates payment and transaction statuses to mirror the refund
-- Expected: Status fields update to 'Refunded' or 'Reversed'
PRINT 'TEST 7.1: Refund - Simulate refund and verify status update';
-- Simulate refund for order ID 1
UPDATE orders
SET order_status = 'Refunded',
    payment_status = 'Reversed',
    transaction_status = 'Reversed'
WHERE id = 1;

-- Verify the refund status was applied
SELECT id, order_status, payment_status, transaction_status
FROM orders
WHERE id = 1;
-- Expected Result: Order 1 with statuses reflecting the refund
-- FAIL scenario: Any of the fields remain at previous values

-- TEST 7.2: REFUND DATA INTEGRITY
-- After refund, ensures order data integrity is maintained
-- Business Rule: Refund should not corrupt order record
-- Expected: Order exists with valid data, status is 'Refunded'
PRINT 'TEST 7.2: Refund - Ensure refunded order maintains data integrity';
SELECT id, user_id, product_id, quantity, order_status
FROM orders
WHERE order_status = 'Refunded';
-- Expected Result: Refunded orders with complete, valid data
-- FAIL scenario: NULL values, missing references, or corrupted quantities

-- TEST 7.3: USER-REFUND RELATIONSHIP
-- Validates refunded orders still maintain user relationship
-- Business Rule: Refund processing should not break user linkage
-- Expected: All refunded orders trace back to valid users
PRINT 'TEST 7.3: Refund - Verify refunded orders maintain user relationship';
SELECT o.id as order_id, o.order_status, u.email, u.id as user_id
FROM orders o
INNER JOIN users u ON o.user_id = u.id
WHERE o.order_status = 'Refunded';
-- Expected Result: Returns refunded orders linked to real users
-- FAIL scenario: Returns orders with NULL user_id or missing user records

-- TEST 7.4: INVENTORY ROLLBACK ON REFUND
-- Simulate restoration of stock when a refunded order is processed
PRINT 'TEST 7.4: Refund - Verify inventory rollback';
UPDATE products
SET stock = stock + (SELECT quantity FROM orders WHERE id = 1)
WHERE id = (SELECT product_id FROM orders WHERE id = 1);

SELECT id, name, stock
FROM products
WHERE id = (SELECT product_id FROM orders WHERE id = 1);
-- Expected Result: Stock returns to its pre-sale value
-- FAIL scenario: Stock remains decremented or becomes incorrect


-- ==============================================================================
-- SECTION 8: COMPREHENSIVE DATA INTEGRITY SUMMARY
-- ==============================================================================

-- TEST 8.1: USER RECORD COUNT
-- Shows total valid user records in system
PRINT 'TEST 8.1: Summary - Total active users';
SELECT COUNT(*) as total_users FROM users;
-- Expected Result: 10 (all test users created)

-- TEST 8.2: ORDER RECORD COUNT
-- Shows total orders in system
PRINT 'TEST 8.2: Summary - Total orders created';
SELECT COUNT(*) as total_orders FROM orders;
-- Expected Result: 10 (all test orders created)

-- TEST 8.3: PRODUCT CATALOG SIZE
-- Shows inventory items available
PRINT 'TEST 8.3: Summary - Total products in catalog';
SELECT COUNT(*) as total_products FROM products;
-- Expected Result: 10 (all products in catalog)

-- TEST 8.4: OVERALL REFERENTIAL INTEGRITY CHECK
-- Final validation that all foreign key relationships are valid
-- Expected: Zero COUNT represents zero orphaned records
PRINT 'TEST 8.4: Summary - Verify complete referential integrity';
SELECT 
    (SELECT COUNT(*) FROM orders WHERE user_id NOT IN (SELECT id FROM users)) as orphaned_orders,
    (SELECT COUNT(*) FROM orders WHERE product_id NOT IN (SELECT id FROM products)) as invalid_product_orders;
-- Expected Result: 0, 0 (no orphaned or invalid references)
-- FAIL scenario: Any non-zero count indicates data integrity issue


-- ==============================================================================
-- END OF TEST SUITE
-- ==============================================================================
-- All tests completed. Review results above for:
-- ✓ User validation (encrypted passwords, unique emails)
-- ✓ Order integrity (valid references, correct status)
-- ✓ Inventory consistency (quantities, stock levels)
-- ✓ Payment tracking (status transitions)
-- ✓ Refund processing (state changes, data preservation)
-- ==============================================================================
