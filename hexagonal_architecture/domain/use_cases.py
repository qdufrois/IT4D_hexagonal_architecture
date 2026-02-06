from uuid import UUID

from hexagonal_architecture.domain.entities import Customer, PetType
from hexagonal_architecture.ports.customers_repository import get_customers_repository


def get_customer_allowed_to_trade_in(customer_id: UUID) -> Customer:
    """
    Returns the customer allowed to perform a trade in.

    Raises:
        HTTPForbidden: if the customer is not allowed
    """

    customers_repository = get_customers_repository()
    customer = customers_repository.get(customer_id)

    if customer.age < 18:
        raise HTTPForbidden("Customer is not an adult")

    if customer.address.country not in ["US", "FR", "DE", "IT", "ES", "UK"]:
        raise HTTPForbidden("Customer is not from a supported country")

    if customer.owned_pet.type not in [PetType.DOG, PetType.CAT]:
        raise HTTPForbidden("Customer must have a dog or a cat")

    return customer
