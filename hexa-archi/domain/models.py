from dataclasses import dataclass

@dataclass
class Customer:
    id: str
    age: int
    country: str
    owned_pet: str