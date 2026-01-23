from enum import StrEnum

from hexagonal_architecture.domain.trade_in import TradeInDomainEntity


class PetType(StrEnum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    GUINEA_PIG = "guinea_pig"


class Pet(TradeInDomainEntity):
    type: PetType

    def can_trade_in(self):
        return self.type in [PetType.DOG, PetType.CAT]
