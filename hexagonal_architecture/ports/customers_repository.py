from uuid import UUID

from hexagonal_architecture.domain.entities import Customer


class CustomersRepository:
    def get(self, id: UUID) -> Customer:
        raise NotImplementedError()


def get_customers_repository() -> CustomersRepository:
    from hexagonal_architecture.adapters.customers_adapter import CustomersAdapter
    return CustomersAdapter()
