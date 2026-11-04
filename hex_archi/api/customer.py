from http.client import HTTPException

from hex_archi.domain.ports import get_customer_port
from hex_archi.domain.use_case import CustomerNotAllowed, validate_customer

class GetCustomerResponse(BaseModel):
    id: str
    age: int
    name: str


@router.get("/customer/{customer_id}")
def get_customer(customer_id: str):
    """
    Get customer information by ID
    """
    customer_entity = get_customer_port(customer_id)
    try:
        validate_customer(customer_entity)
    except CustomerNotAllowed as e:
        raise HTTPException(status_code=403, detail=str(e))

    return GetCustomerResponse(
        id=customer_id,
        age=customer_entity.age,
        name=customer_entity.name,
    )
