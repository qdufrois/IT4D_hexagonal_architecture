from typing import Protocol

from hex_archi.domain.entity import CustomerEntity


class CustomerAddressRecord(Protocol):
    country: str


class CustomerRecord(Protocol):
    age: int
    address: CustomerAddressRecord
    owned_pet: str


class CustomerManager(Protocol):
    def get(self, **kwargs: object) -> CustomerRecord: ...


class DjangoCustomerRepository:
    def __init__(self, customer_manager: CustomerManager) -> None:
        self._customer_manager = customer_manager

    def get_by_id(self, customer_id: str) -> CustomerEntity:
        customer = self._customer_manager.get(pk=customer_id)
        return CustomerEntity(
            age=customer.age,
            address_country=customer.address.country,
            owned_pet=customer.owned_pet,
        )
