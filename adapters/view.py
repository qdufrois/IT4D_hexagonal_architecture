
class GetAllowedCustomerView(View): 
    def __init__(self, use_case: GetAllowedCustomerUseCase) -> None:
        self.use_case = use_case

    def get(self, URL):
        customer_id = int(URL.split("/")[-1])

        try:
            customer = self.use_case.get_customer_info(customer_id) 
        except Exception as e:
            raise HTTP.forbidden(str(e))

        return CustomerSerializer(customer)