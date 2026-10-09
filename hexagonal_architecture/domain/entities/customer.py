from dataclasses import dataclass


SUPPORTED_COUNTRIES = {"US", "FR", "DE", "IT", "ES", "UK"}
SUPPORTED_PETS = {"dog", "cat"}

# Domain Exceptions
class CustomerNotEligible(Exception):
    pass

@dataclass
class Address:
    country: str

@dataclass
class Customer:
    id: str
    name: str
    age: int
    owned_pet: str | None
    address_id: Address

    def ensure_trade_in_eligibility(self) -> None:
        if self.age < 18:
            raise CustomerNotEligible("Customer is not an adult")
        if self.address_id.country not in SUPPORTED_COUNTRIES:
            raise CustomerNotEligible("Customer is not from a supported country")
        if self.owned_pet not in SUPPORTED_PETS:
            raise CustomerNotEligible("Customer must have a dog or a cat")
