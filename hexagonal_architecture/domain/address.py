from enum import StrEnum
from uuid import UUID

from hexagonal_architecture.domain.trade_in import TradeInDomainEntity


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


class Address(TradeInDomainEntity):
    id: UUID
    country: Country

    def can_trade_in(self):
        return self.country.value in ["US", "FR", "DE", "IT", "ES", "UK"]
