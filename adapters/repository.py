from domain.entity import Address, Country, Customer, PetType
from domain.ports import CustomerRepository

class DjangoORMCustomerRepository(CustomerRepository):
    def get_customer(self, customer_id: int) -> Customer:
        db_customer = CustomerModel.objects.get(id=customer_id)
        try:
            country = Country(db_customer.address_id.country)
        except ValueError:
            country = None

        try:
            pet = PetType(db_customer.owned_pet)
        except ValueError:
            pet = None

        address = Address(id=db_customer.address_id.id, country=country)

        return Customer(
            id=db_customer.id,
            age=db_customer.age,
            address=address,
            owned_pet=pet,
        )
        