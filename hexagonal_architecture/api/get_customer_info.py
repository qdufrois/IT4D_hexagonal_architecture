from hexagonal_architecture.domain.use_cases import get_customer_allowed_to_trade_in


class GetAllowedCustomerView(View):
    """
    Only specific customers are allowed to do a trade-in
    """

    def get(self, URL):
        customer_id = URL.split("/")[-1]

        customer = get_customer_allowed_to_trade_in(customer_id)

        return CustomerSerializer(customer)
