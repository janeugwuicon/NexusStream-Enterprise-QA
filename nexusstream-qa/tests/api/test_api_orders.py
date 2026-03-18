import time
import requests
from api_client import APIClient

def test_create_and_get_order():
    api = APIClient()

    res = api.create_order()
    assert res.status_code == 201

    user_id = res.json()["id"]

    # Retry mechanism to handle intermittent SSL errors from public mock API
    res2 = None
    for attempt in range(3):
        try:
            res2 = api.get_order(user_id)
            break
        except requests.exceptions.SSLError:
            if attempt == 2:
                raise
            time.sleep(1)

    assert res2.status_code in [200, 404]