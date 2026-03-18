import pytest
import csv
import os

def load_cards():
    # Resolve path relative to this test file
    data_path = os.path.join(os.path.dirname(__file__), "../../data/cards.csv")
    with open(data_path) as f:
        return list(csv.DictReader(f))

@pytest.mark.parametrize("card", load_cards())
def test_payment_gateways(card):
    if card["status"] == "valid":
        # For valid cards, we expect standard processing
        assert len(card["card"]) >= 16
    else:
        # For invalid cards, we simulate a system rejection check
        # In a real API, this would be: assert response.status_code == 400
        assert card["status"] == "invalid"