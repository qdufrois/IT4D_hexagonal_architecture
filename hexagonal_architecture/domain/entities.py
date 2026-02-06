from enum import StrEnum
from uuid import UUID


class PetType(StrEnum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    GUINEA_PIG = "guinea_pig"


class Pet:
    type: PetType


class Country(StrEnum):
    UK = "UK"
    US = "US"
    FR = "FR"
    DE = "DE"
    IT = "IT"
    ES = "ES"
    RU = "RU"
    CZ = "CZ"
    PL = "PL"
    DK = "DK"


class Address:
    id: UUID
    country: Country


class Customer:
    id: UUID
    age: PositiveInt
    address: Address
    owned_pet: Pet
