import requests

def test_invalid_endpoint():
    res = requests.get("https://jsonplaceholder.typicode.com/posts/999999")
    assert res.status_code == 404