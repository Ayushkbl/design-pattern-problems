from typing import Dict, Optional

from domain.payment import Payment

class PaymentRepository:

    def __init__(self):
        self._payments: Dict[str, Payment] = dict()
        self._ticket_to_payments: Dict[str, list[str]] = dict()
    
    def save(self, payment: Payment) -> Payment:
        self._payments[payment.id] = payment
        if payment.ticket_id not in self._ticket_to_payments:
            self._ticket_to_payments[payment.ticket_id] = []
        self._ticket_to_payments[payment.ticket_id].append(payment.id)
        return payment
    
    def find_by_id(self, payment_id: str) -> Optional[Payment]:
        return self._payments.get(payment_id)
    
    def find_by_ticket_id(self, ticket_id: str) -> list[Payment]:
        payment_ids = self._ticket_to_payments.get(ticket_id, [])
        return [self._payments[pid] for pid in payment_ids if pid in self._payments]
    
    def find_all(self) -> list[Payment]:
        return list(self._payments.values())
    
    def update(self, payment: Payment) -> None:
        if payment.id in self._payments:
            self._payments[payment.id] = payment
    
    def delete(self, payment_id: str) -> None:
        payment = self._payments.pop(payment_id, None)
        if payment:
            self._ticket_to_payments[payment.ticket_id].remove(payment_id)
    
    def clear(self) -> None:
        self._payments.clear()
        self._ticket_to_payments.clear()