

from movie_ticket.location.seat import Seat
from movie_ticket.showing.screening import Screening


class Ticket:

    def __init__(self, screening: Screening, seat: Seat, price: float):
        self.__screening = screening
        self.__seat = seat
        self.__price = price
    
    @property
    def screening(self) -> Screening:
        return self.__screening
    
    @property
    def seat(self) -> Seat:
        return self.__seat
    
    @property
    def price(self) -> float:
        return self.__price