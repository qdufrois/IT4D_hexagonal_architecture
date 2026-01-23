from uuid import UUID

from hexagonal_architecture.domain.address import Address
from hexagonal_architecture.domain.pet import Pet
from hexagonal_architecture.domain.trade_in import TradeInDomainEntity


class Customer(TradeInDomainEntity):
    id: UUID
    age: PositiveInt
    address: Address
    owned_pet: Pet

    def can_trade_in(self):
        return self.age >= 18 and self.address.can_trade_in() and self.owned_pet.can_trade_in()
