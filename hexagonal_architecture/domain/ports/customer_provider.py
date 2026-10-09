
from typing import Protocol
from hexagonal_architecture.domain.entities.customer import Customer

class CustomerProvider(Protocol):

    def get_one(self, customer_id: str) -> Customer | None:
        ...