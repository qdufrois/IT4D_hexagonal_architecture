from customer.entities import CustomerInfo
from customer.adapters import get_customer


def get_customer_info(customer_id: int) -> CustomerInfo:
    return get_customer(customer_id)
