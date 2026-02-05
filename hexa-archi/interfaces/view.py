from django.views import View
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotFound

from domain.services import TradeInEligibilityChecker
from domain.exceptions import TradeInEligibilityError
from adapters.repositories import DjangoCustomerRepository
from your_app.models import Customer as CustomerModel


class GetAllowedCustomerView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = DjangoCustomerRepository()
        self.checker = TradeInEligibilityChecker()

    def get(self, request, customer_id: str):
        try:
            customer = self.repository.get_by_id(customer_id)
            self.checker.check(customer)
            return JsonResponse({
                "eligible": True,
                "customer_id": customer.id
            })
        except TradeInEligibilityError as e:
            return HttpResponseForbidden({"error": str(e)})
        except CustomerModel.DoesNotExist:
            return HttpResponseNotFound({"error": "Customer not found"})