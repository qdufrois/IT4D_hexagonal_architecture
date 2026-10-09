from dataclasses import dataclass

from hexagonal_architecture.domain.ports.customer_provider import CustomerProvider
from hexagonal_architecture.domain.use_cases.get_customer import (
    CustomerNotEligible,
    CustomerNotFound,
    get_trade_in_allowed_customer,
)


# API layer exceptions (placeholders for framework exceptions)
class Http404CustomerNotFound(Exception):
    pass


class Http403CustomerForbidden(Exception):
    pass


@dataclass
class CustomerResponseData:
    name: str


@dataclass
class CustomerResponse:
    data: CustomerResponseData


## This would be the api route handler
def router_get_trade_in_allowed_customer(
    customer_id: str,
    customer_provider: CustomerProvider,
) -> CustomerResponse:
    try:
        customer = get_trade_in_allowed_customer(
            customer_id=customer_id,
            customer_provider=customer_provider,
        )
    except CustomerNotFound as exc:
        raise Http404CustomerNotFound(str(exc)) from exc
    except CustomerNotEligible as exc:
        raise Http403CustomerForbidden(str(exc)) from exc

    return CustomerResponse(
        data=CustomerResponseData(name=customer.name)
    )