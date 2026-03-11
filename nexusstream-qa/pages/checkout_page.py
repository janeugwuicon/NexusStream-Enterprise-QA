from .base_page import BasePage


class CheckoutPage(BasePage):

    # checkout page
    PROCEED_CHECKOUT = ".check_out"
    MESSAGE = "textarea[name='message']"
    PLACE_ORDER = "a:has-text('Place Order')"

    # payment page
    NAME = "[data-qa='name-on-card']"
    CARD = "[data-qa='card-number']"
    CVC = "[data-qa='cvc']"
    MONTH = "[data-qa='expiry-month']"
    YEAR = "[data-qa='expiry-year']"
    PAY = "[data-qa='pay-button']"

    SUCCESS = "[data-qa='order-placed']"

    def proceed_to_checkout(self):
        """Click proceed to checkout from cart"""
        self.click(self.PROCEED_CHECKOUT)

    def add_order_message(self, message: str):
        """Add delivery instructions"""
        self.fill(self.MESSAGE, message)

    def place_order(self):
        """Move to payment page"""
        self.click(self.PLACE_ORDER)

    def pay(self, name, card, cvc, month, year):
        """Fill payment form"""

        self.fill(self.NAME, name)
        self.fill(self.CARD, card)
        self.fill(self.CVC, cvc)
        self.fill(self.MONTH, month)
        self.fill(self.YEAR, year)

        self.click(self.PAY)