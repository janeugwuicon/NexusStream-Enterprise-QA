class UserBuilder:
    def __init__(self):
        self.first = "John"
        self.last = "Doe"
        self.zip = "12345"

    def with_zip(self, zip_code: str):
        self.zip = zip_code
        return self

    def build(self):
        return self.first, self.last, self.zip