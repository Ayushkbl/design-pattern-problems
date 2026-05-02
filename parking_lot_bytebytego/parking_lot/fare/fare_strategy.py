from abc import ABC, abstractmethod

from parking_lot.fare.ticket import Ticket

class FareStrategy(ABC):

    @abstractmethod
    def calculate_fare(self, ticket: Ticket, input_fare: float) -> float:
        pass