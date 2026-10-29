from abc import ABC

from django import Customer as DjangoCustomer
from entities import Customer
from UUID import UUID


class CustomerRepo(ABC):
    def get(self, customer_id: UUID) -> Customer: ...


class CustomerDjangoRepo(CustomerRepo):
    def get(self, customer_id: UUID) -> Customer:
        django_customer = DjangoCustomer.objects.get(id=customer_id)  # Using Django ORM
        return self._make_customer_out_of_django_customer(django_customer)

    def _make_customer_out_of_django_customer(
        self,
        django_customer: DjangoCustomer,
    ) -> Customer: ...
