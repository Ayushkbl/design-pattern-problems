import uuid
from enum import Enum

class Payment:
    """
    Payment Domain Model
    
    Represents a payment transaction for a parking ticket.
    """

    class PaymentGateway(Enum):
        RAZORPAY = "RAZORPAY"
        STRIPE = "STRIPE"
    
    class PaymentStatus(Enum):
        PENDING = "PENDING"
        SUCCESS = "SUCCESS"
        FAILED = "FAILED"
    
    def __init__(self, ticket_id: str, amount: float, payment_gateway: PaymentGateway) -> None:
        self.id: str = str(uuid.uuid4())
        self.ticket_id: uuid.UUID = ticket_id
        self.amount: float = amount
        self.gateway: Payment.PaymentGateway = payment_gateway
        self.status: Payment.PaymentStatus = Payment.PaymentStatus.PENDING
    
    def mark_as_success(self) -> None:
        self.status = Payment.PaymentStatus.SUCCESS
    
    def mark_as_failed(self) -> None:
        self.status = Payment.PaymentStatus.FAILED
    
    def __str__(self) -> str:
        return (f"Payment{{id={self.id}"
                f", ticket_id = {self.ticket_id}"
                f", amount = {self.amount}"
                f", payment_gateway = {self.gateway.value}"
                f", status = {self.status.value}}}")