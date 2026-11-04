from hex_archi.domain.entity import CustomerEntity


def get_customer_port(customer_id: str) -> CustomerEntity:

    from hex_archi.adapter.database_queries import DjangoCustomerRepository

    django_customer_repo = DjangoCustomerRepository()
    return django_customer_repo.get_by_id(customer_id)

    