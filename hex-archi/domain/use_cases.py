from domain.customer import ports
from domain.customer.entities import CustomerInfo
from domain.customer.exceptions import CustomerNotAllowed


def get_and_validate_customer(customer_id: int) -> CustomerInfo:
    customer_info = ports.get_customer(customer_id)

    if customer_info.age < 18:
        raise CustomerNotAllowed

    if customer_info.country not in ["US", "FR", "DE", "IT", "ES", "UK"]:
        raise CustomerNotAllowed

    if customer_info.owned_pet not in ["dog", "cat"]:
        raise CustomerNotAllowed

    return customer_info
