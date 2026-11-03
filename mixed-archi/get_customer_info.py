class CustomerNotAllowed (Exception):
     pass




class GetAllowedCustomerView(View): # using Django View
    """
    Only specific customers are allowed to do a trade-in
    """                 
    
    def get(self, URL): 
        customer_id = URL.split("/")[-1]
        customer = get_customer(customer_id)
        customer_entity = CustomerEntity(
             age= customer.age,
             address_id = customer.address_id,
             owned_pet = customer.owned_pet)
        try:
            validate_customer(customer_entity)
        except CustomerNotAllowed as e:
             raise HTTP.forbidden(e)

        return CustomerSerializer(customer) # using Django Serializer
    

# Where is the domain logic?
# the if conditions, business domain
# Where is the data access logic? (driven side)
# Where is the client interface logic? (driving side)
