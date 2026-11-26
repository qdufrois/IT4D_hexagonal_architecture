from domain.entity import Address, Country, Customer, PetType
from domain.ports import CustomerRepository
from domain.use_cases import GetAllowedCustomerUseCase


class FakeCustomerRepository(CustomerRepository):
    def __init__(self, customer: Customer) -> None:
        self.customer = customer

    def get_customer(self, customer_id: int) -> Customer:
        return self.customer


valid_customer = Customer(
    id=1,
    age=23,
    address=Address(id=10, country=Country.FR),
    owned_pet=PetType.Cat,
)
use_case = GetAllowedCustomerUseCase(repository=FakeCustomerRepository(valid_customer))
result = use_case.get_customer_info(1)
print("Test 1 OK! Allowed customer:", result)


young_customer = Customer(
    id=2,
    age=12,
    address=Address(id=11, country=Country.FR),
    owned_pet=PetType.Dog,
)
use_case_2 = GetAllowedCustomerUseCase(repository=FakeCustomerRepository(young_customer))
try:
    use_case_2.get_customer_info(2)
except Exception as e:
    print("Test 2 OK! Blocked underage customer:", e)