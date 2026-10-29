from customer_repository import CustomerRepo
from entities import Customer
from UUID import UUID

ADULT_AGE_THRESHOLD: int = 18
SUPPORTED_COUNTRIES_LIST: list[str] = ["US", "FR", "DE", "IT", "ES", "UK"]


class UnsupportedCountry(Exception): ...


class CustomerNotAdult(Exception): ...


class CustomerHasNoMandatoryPets(Exception): ...


def get_customer_service(customer_id: UUID, customer_repo: CustomerRepo):
    customer = customer_repo.get(customer_id)
    if not is_customer_adult(customer):
        raise CustomerNotAdult(f"Customer {customer_id} is not an Adult.")
    if not is_customer_living_in_supported_country(customer):
        raise UnsupportedCountry(
            f"Customer {customer_id} lives in {customer.address.country}, which is not supported."
        )
    if not is_customer_owning_mandatory_pet(customer):
        raise CustomerHasNoMandatoryPets(
            f"Customer {customer_id} does not share his life with a mandatory pet."
        )
    return customer


def is_customer_adult(customer: Customer) -> bool:
    return customer.age > ADULT_AGE_THRESHOLD


def is_customer_owning_mandatory_pet(customer: Customer) -> bool:
    return customer.mandatory_pet != None


def is_customer_living_in_supported_country(customer: Customer) -> bool:
    # Open question: is this a business check or a data validity check that would belong into the repository ?
    return customer.address.country in SUPPORTED_COUNTRIES_LIST
