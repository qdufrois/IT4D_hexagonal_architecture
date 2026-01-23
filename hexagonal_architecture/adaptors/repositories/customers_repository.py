from uuid import UUID

from hexagonal_architecture.domain.customer import Customer


class CustomersRepository:
    def get(self, id: UUID) -> Customer:
        return CustomerTable.objects.get(id=id)
