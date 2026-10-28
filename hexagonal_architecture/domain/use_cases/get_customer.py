from hexagonal_architecture.domain.entities.customer import Customer
from hexagonal_architecture.domain.ports.customer_provider import CustomerProvider


class CustomerNotFound(Exception):
    pass

class CustomerNotEligible(Exception):
    pass


def get_trade_in_allowed_customer(customer_id: str, customer_provider: CustomerProvider) -> Customer:
    customer = customer_provider.get_one(customer_id)

    if customer is None:
        raise CustomerNotFound("Customer not found")

    customer.ensure_trade_in_eligibility()

    return customer
