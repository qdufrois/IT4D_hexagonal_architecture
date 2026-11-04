from hex_archi.domain.entity import CustomerEntity


class CustomerNotAllowed(Exception):
    pass





def validate_customer(customer: CustomerEntity):
    if customer.age < 18:
        raise CustomerNotAllowed("Customer is not an adult")

    if customer.address_id.country not in ["US", "FR", "DE", "IT", "ES", "UK"]:
        raise CustomerNotAllowed("Customer is not from a supported country")

    if customer.owned_pet not in ["dog", "cat"]:
        raise CustomerNotAllowed("Customer must have a dog or a cat")
