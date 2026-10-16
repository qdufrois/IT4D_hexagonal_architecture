import pytest

from hexagonal_architecture.domain.entities.customer import Customer, CustomerNotEligible
from hexagonal_architecture.domain.entities.customer import Address
from hexagonal_architecture.domain.use_cases.get_customer import CustomerNotFound, get_trade_in_allowed_customer


def test_get_trade_in_allowed_customer_found_eligible() -> None:
    "Nominal test. WHen an existing "

    # GIVEN
    customer_id="existing_id"

    class FakeCustomerProvider:
        def get_one(self, customer_id: str) -> Customer | None:
            return Customer(
                id="existing_id",
                name="fake_name",
                age=34,
                owned_pet="dog",
                address_id=Address(country="ES")
            )

    # WHEN
    customer = get_trade_in_allowed_customer(customer_id, FakeCustomerProvider())

    # THEN
    assert customer.id == customer_id

@pytest.mark.parametrize("non_valid_pet", ["panda", "horse", "koala"])
def test_get_trade_in_allowed_customer_found_not_eligigle(non_valid_pet: str) -> None:
    "Nominal test. WHen an existing "

    # GIVEN
    customer_id="existing_id"

    class FakeCustomerProvider:
        def get_one(self, customer_id: str) -> Customer | None:
            return Customer(
                id="existing_id",
                name="fake_name",
                age=34,
                owned_pet=non_valid_pet, # Not eligible
                address_id=Address(country="ES")
            )


    # WHEN / THEN
    with pytest.raises(CustomerNotEligible, match="Customer must have a dog or a cat"):
        get_trade_in_allowed_customer(customer_id, FakeCustomerProvider())

def test_get_trade_in_allowed_customer_not_found() -> None:
    """Raise CustomerNotFound when the customer doesn't exist."""

    # GIVEN
    customer_id = "non_existing_id"

    class FakeCustomerProvider:
        def get_one(self, customer_id: str) -> Customer | None:
            return None

    # WHEN / THEN
    with pytest.raises(CustomerNotFound, match="Customer not found"):
        get_trade_in_allowed_customer(customer_id, FakeCustomerProvider())