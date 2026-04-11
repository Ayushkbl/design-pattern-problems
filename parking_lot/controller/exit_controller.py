from typing import Optional, NamedTuple
from service.payment_service import PaymentService
from service.receipt_service import ReceiptService
from service.pricing_service import PricingService
from service.slot_service import SlotService
from service.ticket_service import TicketService

class ExitResult(NamedTuple):
    success: bool
    receipt_id: Optional[str]
    fee: float
    message: str

class ExitController:

    def __init__(self, ticket_service: TicketService, payment_service: PaymentService,
                 receipt_service: ReceiptService, pricing_service: PricingService,
                 slot_service: SlotService):
        
        self._ticket_service = ticket_service
        self._payment_service = payment_service
        self._receipt_service = receipt_service
        self._pricing_service = pricing_service
        self._slot_service = slot_service
        print("[CONTROLLER] ExitController initialized")
    
    def exit_vehicle(self, ticket_id: str) -> ExitResult:
        print(f"[CONTROLLER] Exit vehicle request - Ticket: {ticket_id}")
        ticket = self._ticket_service.get_ticket(ticket_id)
        if not ticket:
            return ExitResult(False, None, 0.0, "Ticket not found")
        
        if not ticket.active:
            return ExitResult(False, None, 0.0, "Ticket is not active")
        
        fee = self._pricing_service.calculate_fee(ticket)
        if not self._payment_service.process_payment_with_retry(ticket_id, fee, 3):
            return ExitResult(False, None, fee, "Payment Failed")
        
        receipt = self._receipt_service.generate_receipt(ticket, fee)
        self._receipt_service.mark_receipt_as_paid(receipt)
        self._slot_service.release_slot(ticket.slot_id)
        self._ticket_service.deactivate_ticket(ticket_id)

    def generate_receipt_text(self, ticket_id: str) -> str:
        ticket = self._ticket_service.get_ticket(ticket_id)
        if not ticket:
            return "Ticket not found"
        
        fee = self._pricing_service.calculate_fee(ticket)
        receipt = self._receipt_service.generate_receipt(ticket, fee)
        return self._receipt_service.generate_receipt_text(receipt, ticket)