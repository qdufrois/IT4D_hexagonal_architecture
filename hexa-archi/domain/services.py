from .exceptions import TradeInEligibilityError
from .models import Customer


class TradeInEligibilityChecker:

    SUPPORTED_COUNTRIES = ["US", "FR", "DE", "IT", "ES", "UK"]
    ALLOWED_PETS = ["dog", "cat"]
    MINIMUM_AGE = 18

    def check(self, customer: Customer) -> None:
        """
        check if customer meets trade-in requirements.
        raises TradeInEligibilityError if not eligible.
        """
        if customer.age < self.MINIMUM_AGE:
            raise TradeInEligibilityError("Customer is not an adult")

        if customer.country not in self.SUPPORTED_COUNTRIES:
            raise TradeInEligibilityError("Customer is not from a supported country")

        if customer.owned_pet not in self.ALLOWED_PETS:
            raise TradeInEligibilityError("Customer must have a dog or a cat")