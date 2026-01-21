class GetAllowedCustomerView(View): # using Django View
    """
    Only specific customers are allowed to do a trade-in
    """                 
    
    def get(self, URL): 
        curstomer_id = URL.split("/")[-1]
        customer = Customer.objects.get(id=curstomer_id) # using Django ORM

        if customer.age < 18: 
            raise HTTP.forbidden("Customer is not an adult") 
        
        if customer.address_id.country not in ["US", "FR", "DE", "IT", "ES", "UK"]:
            raise HTTP.forbidden("Customer is not from a supported country")
        
        if customer.owned_pet not in ["dog", "cat"]:
            raise HTTP.forbidden("Customer must have a dog or a cat")

        return CustomerSerializer(customer) # using Django Serializer
    

# Where is the domain logic?
# Where is the data access logic? (driven side)
# Where is the client interface logic? (driving side)
