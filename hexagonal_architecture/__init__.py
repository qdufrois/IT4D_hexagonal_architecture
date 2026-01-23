"""
Domain logic:
- Customer(id, age, address_id, owned_pet)
- Address(id, country)
- Pet(name)
- Customers allowed to do a Trade-in
    age >= 18, address country in a supported country, owned_pet is cat or dog

Data access logic: Django ORM

Client interface logic:
- checking if customer is allowed to do trade-in
- else: raise HTTPForbiddenError with reason
"""