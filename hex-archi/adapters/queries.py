from adapters.models import CustomerDataModel
from domain.customer.entities import CustomerInfo


class CustomerRepository:
    def get_customer(self, customer_id) -> CustomerDataModel:
        return CustomerDataModel.objects.get(id=customer_id)


class CustomerSerializer:
    def init(self, customer: CustomerDataModel):
        self.customer = customer

    def serialize(self) -> CustomerInfo:
        return CustomerInfo(
            name=f"{self.customer.first_name} {self.customer.last_name}",
            age=self.customer.age,
            country=self.customer.country,
            owned_pet=self.owned_pet,
            hobbies=[self.customer.hobby],
        )


def get_customer(customer_id: int) -> CustomerInfo:
    customer = CustomerRepository().get_customer(customer_id)
    return CustomerSerializer(customer).serialize()
