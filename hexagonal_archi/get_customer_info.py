from uuid import UUID

from customer_repository import CustomerDjangoRepo
from django import HTTP, CustomerSerializer, View
from get_customer_service import (
    CustomerHasNoMandatoryPets,
    CustomerNotAdult,
    UnsupportedCountry,
    get_customer_service,
)


class GetAllowedCustomerView(View):  # using Django View
    """
    Only specific customers are allowed to do a trade-in
    """

    def get(self, URL):
        customer_id = URL.split("/")[-1]
        try:
            customer = get_customer_service(UUID(customer_id), CustomerDjangoRepo())
        except (CustomerNotAdult, CustomerHasNoMandatoryPets, UnsupportedCountry) as e:
            raise HTTP.forbidden from e

        return CustomerSerializer(customer)  # using Django Serializer
