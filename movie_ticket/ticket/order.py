from datetime import datetime
from typing import List

from movie_ticket.ticket.ticket import Ticket

class Order:

    def __init__(self, order_date: datetime):
        self.__ticket: List[Ticket] = []
        self.__order_date = order_date
    
    def add_ticket(self, ticket: Ticket):
        self.__ticket.append(ticket)

    def calculate_total_price(self) -> float:
        return sum(ticket.price or 0 for ticket in self.__ticket)
    
    @property
    def all_tickets(self) -> List[Ticket]:
        return self.__ticket
    
    @property
    def order_date(self) -> datetime:
        return self.__order_date