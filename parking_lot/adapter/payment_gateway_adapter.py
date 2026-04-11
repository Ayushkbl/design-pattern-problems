from abc import ABC, abstractmethod

class PaymentGatewayAdapter(ABC):
    """
    PaymentGatewayAdapter Interface

    Abstract base class for Payment Gateway Adapters.
    """

    @abstractmethod
    def pay(self, ticket_id: str, amount: float) -> bool:
        pass