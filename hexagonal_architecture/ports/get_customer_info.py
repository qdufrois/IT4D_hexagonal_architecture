from hexagonal_architecture.adaptors.repositories.customers_repository import CustomersRepository


class GetAllowedCustomerView(View):
    """
    Only specific customers are allowed to do a trade-in
    """

    def get(self, URL):
        customer_id = URL.split("/")[-1]

        with CustomersRepository() as customers_repository:
            customer = customers_repository.get(customer_id)

        if not customer.can_trade_in():
            raise HTTPForbiddenError()  # TODO: allow trade in ineligibility reasons to be passed onto the error response

        return CustomerSerializer(customer)
