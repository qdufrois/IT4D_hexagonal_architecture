from domain.entity import Customer
from domain.ports import CustomerRepository

class GetAllowedCustomerUseCase:
    def __init__(self, repository: CustomerRepository) -> None:
        self.repository = repository 

    def get_customer_info(self, customer_id: int) -> Customer:
        customer = self.repository.get_customer(customer_id)
        customer.allowed_customer()
        return customer