


from hexagonal_architecture.domain.entities.customer import Address, Customer

DATA = {
    "1": {'id': '1', 'name': 'Mikel', 'age': 34, 'country_code': "ES", 'pet': 'dog'},
    "2": {'id': '2', 'name': 'Mess', 'age': 39, 'country_code': "AR", 'pet': None}
}


class CustomerInMemoryRepository:

    def get_one(self, customer_id: str) -> Customer | None:

        customer_data = DATA.get(customer_id)

        if customer_data is None :
            return None
        
        return Customer(
            id=customer_data["id"],
            name=customer_data["name"],
            age=customer_data["age"],
            owned_pet=customer_data["pet"],
            address_id=Address(country=customer_data["country_code"]),
        )