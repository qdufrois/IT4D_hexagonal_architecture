from fastapi import APIRouter
from fastapi import Request
from http import HTTPStatus
from http.client import HTTPException


from api.schemas import CustomerResponse
from domain.use_cases import get_and_validate_customer
from domain.customer.exceptions import CustomerNotAllowed

router = APIRouter()


@router.get(
    "/customer",
    status_code=HTTPStatus.OK,
)
def get_customer(request: Request, customer_id: int) -> CustomerResponse:
    try:
        customer_info = get_and_validate_customer(customer_id=customer_id)
    except CustomerNotAllowed:
        raise HTTPException(status=HTTPStatus.FORBIDDEN)
    return CustomerResponse.to_response(customer_info)
