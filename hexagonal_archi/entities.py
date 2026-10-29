from dataclasses import dataclass
from enum import Enum
from uuid import UUID


class MandatoryPet(Enum, str):
    DOG = "dog"
    CAT = "cat"


@dataclass
class Address:
    house_number: str
    street_name: str
    postal_code: str
    city: str
    country: str


@dataclass
class Customer:
    customer_id: UUID
    age: int
    address: Address
    mandatory_pet: MandatoryPet | None
