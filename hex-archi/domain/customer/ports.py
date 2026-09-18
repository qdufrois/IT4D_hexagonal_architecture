from customer.entities import CustomerInfo


def get_customer(customer_id: int) -> CustomerInfo:
    from adapters.queries import get_customer_from_database

    return get_customer_from_database(customer_id)
