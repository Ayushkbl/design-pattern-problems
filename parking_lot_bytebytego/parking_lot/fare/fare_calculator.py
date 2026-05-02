from parking_lot.fare.fare_strategy import FareStrategy
from parking_lot.fare.ticket import Ticket

class FareCalculator:

    def __init__(self, fare_strategies: list[FareStrategy]):
        self._fare_strategies = fare_strategies
    
    def calculate_fare(self, ticket: Ticket):
        fare: float = 0.0
        for strategy in self._fare_strategies:
            fare = strategy.calculate_fare(ticket, fare)
        
        return fare
