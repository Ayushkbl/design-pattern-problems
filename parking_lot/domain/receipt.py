import uuid
from enum import Enum
from datetime import datetime

class Receipt:
    """
    Receipt Domain Model
    
    Issued at vehicle exit after payment.
    """

    class PaymentStatus(Enum):
        PENDING = "PENDING"
        SUCCESS = "SUCCESS"
        FAILED = "FAILED"
    
    def __init__(self, ticket_id: str, total_fee: float) -> None:
        self.id: str = str(uuid.uuid4())
        self.ticket_id: str = ticket_id
        self.total_fee: float = total_fee
        self.exit_time: datetime = datetime.now()
        self.payment_status: Receipt.PaymentStatus = Receipt.PaymentStatus.PENDING
    
    def mark_as_paid(self) -> None:
        self.payment_status = Receipt.PaymentStatus.SUCCESS
    
    def mark_as_failed(self) -> None:
        self.payment_status = Receipt.PaymentStatus.FAILED

    def __str__(self) -> str:
        return (f"Receipt{{id={self.id}"
                f"ticket_id={self.ticket_id}"
                f"exit_time={self.exit_time}"
                f"total_fee={self.total_fee}"
                f"payment_status={self.payment_status.value}}}")