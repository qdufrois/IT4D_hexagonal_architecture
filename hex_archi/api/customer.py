from http.client import HTTPException

from hex_archi.domain.entity import CustomerEntity
from hex_archi.domain.use_case import CustomerNotAllowed, validate_customer


@router.get("/customer/{customer_id}")
def get_customer(customer_id: str):
    """
    Get customer information by ID
    """
    customer = get_customer(customer_id)
    customer_entity = CustomerEntity(age=customer.age, address_id=customer.address_id, owned_pet=customer.owned_pet)
    try:
        validate_customer(customer_entity)
    except CustomerNotAllowed as e:
        raise HTTPException(status_code=403, detail=str(e))

    return CustomerSerializer(customer)
