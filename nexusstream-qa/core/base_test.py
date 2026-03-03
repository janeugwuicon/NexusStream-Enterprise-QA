import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page