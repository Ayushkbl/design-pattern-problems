from datetime import datetime

from parking_lot.fare.fare_strategy import FareStrategy
from parking_lot.fare.ticket import Ticket

class PeakHoursFareStrategy(FareStrategy):

    PEAK_HOURS_MULTIPLIER: float = 1.5

    def calculate_fare(self, ticket: Ticket, input_fare: float) -> float:
        fare = input_fare

        if self.is_peak_hours(ticket.entry_time):
            fare = fare * PeakHoursFareStrategy.PEAK_HOURS_MULTIPLIER
        
        return fare

    def is_peak_hours(self, time: datetime):
        hour = time.hour
        return (7 <= hour <= 10 ) or (16 <= hour <= 19)