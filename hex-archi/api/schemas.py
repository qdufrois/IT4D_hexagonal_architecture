from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from domain.customer.entities import CustomerInfo


class CustomerResponse(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, frozen=True, populate_by_name=True)

    name: str
    age: int
    country: str

    @classmethod
    def to_response(cls, customer_info: CustomerInfo) -> "CustomerResponse":
        return CustomerResponse(name=customer_info.name, age=customer_info.age, country=customer_info.country)
