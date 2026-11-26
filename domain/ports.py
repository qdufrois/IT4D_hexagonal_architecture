from abc import ABC, abstractmethod
from domain.entity import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def get_customer(self, customer_id: int) -> Customer : 
        pass

