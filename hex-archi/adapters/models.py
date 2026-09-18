from django import Model


class CustomerDataModel(Model):
    id: int
    first_name: str
    last_name: str
    age: int
    country: str
    owned_pet: str
    hobby: str
