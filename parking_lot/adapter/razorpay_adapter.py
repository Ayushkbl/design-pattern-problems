import random

from .payment_gateway_adapter import PaymentGatewayAdapter

class RazorPayAdapter(PaymentGatewayAdapter):
    """
    RazorpayAdapter
    
    Simulates payment via Razorpay (90% success rate).
    """

    def pay(self, ticket_id: str, amount: float) -> bool:
        print(f"[ADAPTER] RazorpayAdapter processing paymnet for ticket_id: {ticket_id} amount: {amount}")
        success = random.random() < 0.9
        print(f"[ADAPTER] RazorpayAdapter result: {'SUCCESS' if success else 'FAILED'}")
        return success