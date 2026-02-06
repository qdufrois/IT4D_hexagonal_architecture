from uuid import UUID

from hexagonal_architecture.domain.entities import Customer
from hexagonal_architecture.ports.customers_repository import CustomersRepository


class CustomersAdapter(CustomersRepository):
    def get(self, id: UUID) -> Customer:
        customer_dbo = CustomerTable.objects.get(id=id)
        return Customer(
            id=customer_dbo.id,
            age=customer_dbo.age,
            address=customer_dbo.address.as_entity(),
            owned_pet=customer_dbo.owned_pet,
        )
