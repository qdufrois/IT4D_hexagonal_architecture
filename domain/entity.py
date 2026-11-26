from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class PetType(Enum):
    Dog = "dog"
    Cat = "cat"

class Country(Enum):
    US = "US"
    FR = "FR" 
    DE = "DE"
    IT = "IT"
    ES = "ES"
    UK = "UK"

@dataclass
class Address():
    id: int
    country: Country | None

@dataclass
class Customer():
    id: int
    age: int
    address: Address
    owned_pet: PetType

    def __post_init__(self) -> None:
        if self.age <= 0:
            raise ValueError("Age must be positive")

    def allowed_customer(self):
        if self.age < 18:
            raise Exception("You must be at least 18 to trade-in.")

        if self.address.country is None:
            raise Exception("Invalid address.")
        
        if self.owned_pet not in PetType:
            raise Exception("You must own a pet to trade-in.")