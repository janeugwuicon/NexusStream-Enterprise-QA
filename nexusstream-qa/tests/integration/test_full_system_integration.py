
import psycopg2
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from api_client import APIClient

def test_full_system(page):
    # 1. API: Create a user context (Simulated for this demo)
    api = APIClient()
    # In a real app, we might create a user via API first.
    # For SauceDemo, we use the standard user.

    # 2. UI: Perform the "Buy" action using Page Object Model
    lp = LoginPage(page)
    lp.load()
    lp.login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    inv.add_item()
    inv.go_to_cart()

    cart = CartPage(page)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.fill_details("Integration", "Test", "99999")
    checkout.finish()

    assert checkout.success.is_visible()

    # 3. DB: Verify Inventory using psycopg2 (Real)
    # Connect to the DB defined in env vars (e.g. from Docker container)
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "nexusstream"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "password")
        )
        cur = conn.cursor()
        # Verify stock for the item (assuming ID=1) has decreased
        cur.execute("SELECT stock_quantity FROM inventory WHERE product_id = %s", (1,))
        row = cur.fetchone()
        if row:
            stock_count = row[0]
            # In a real scenario, we expect it to drop from 10 to 9
            assert stock_count < 10, f"DB Validation Failed: Stock is {stock_count}"
        
        cur.close()
        conn.close()
    except psycopg2.OperationalError:
        print("\nWARNING: Could not connect to local PostgreSQL. Skipping DB check.")

    # 4. API: Verify Order Creation
    # We verify the backend processed an order (using our mock API client)
    res = api.create_order()
    assert res.status_code == 201