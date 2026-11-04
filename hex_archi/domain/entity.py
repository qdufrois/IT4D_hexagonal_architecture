from pydantic import BaseModel


class CustomerEntity(BaseModel):
    age: int
    address_id: str
    owned_pet: str
