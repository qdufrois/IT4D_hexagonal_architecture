from domain.ports import CustomerRepository
from domain.models import Customer


class DjangoCustomerRepository(CustomerRepository):
    """Repo adapter - implements the port CustomerRepository"""

    def get_by_id(self, customer_id: str) -> Customer:
        """Fetch customer from database and convert to domain model"""
        django_customer = CustomerModel.objects.get(id=customer_id)

        # Django ORM model → domain model
        return Customer(
            id=str(django_customer.id),
            age=django_customer.age,
            country=django_customer.address_id.country,
            owned_pet=django_customer.owned_pet
        )