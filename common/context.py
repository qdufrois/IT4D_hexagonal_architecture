from adapters.repository import DjangoORMCustomerRepository
from adapters.view import GetAllowedCustomerView
from domain.use_cases import GetAllowedCustomerUseCase


def build_customer_view() -> GetAllowedCustomerView:
    repository = DjangoORMCustomerRepository()

    use_case = GetAllowedCustomerUseCase(repository=repository)

    view = GetAllowedCustomerView(use_case=use_case)

    return view