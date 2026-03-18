import requests
from config import API_URL

class APIClient:
    def create_order(self):
        # Using /posts to simulate creating an order on a stable mock API
        return requests.post(f"{API_URL}/posts", json={"title": "Order 123", "body": "test order", "userId": 1})

    def get_order(self, order_id):
        return requests.get(f"{API_URL}/posts/{order_id}")

    def login(self, email, password):
        return requests.post(
            f"{API_URL}/login",
            json={"email": email, "password": password}
        )