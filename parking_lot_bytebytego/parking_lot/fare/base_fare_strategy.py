from parking_lot.fare.fare_strategy import FareStrategy
from parking_lot.fare.ticket import Ticket
from parking_lot.vehicle.vehicle_size import VehicleSize

class BaseFareStrategy(FareStrategy):

    SMALL_VEHICLE_RATE: float = 1.0
    MEDIUM_VEHICLE_RATE: float = 2.0
    LARGE_VEHICLE_RATE: float = 3.0

    def calculate_fare(self, ticket: Ticket, input_fare: float) -> float:
        
        fare = input_fare
        if ticket.vehicle.vehicle_size == VehicleSize.SMALL:
            rate = BaseFareStrategy.SMALL_VEHICLE_RATE
        elif ticket.vehicle.vehicle_size == VehicleSize.MEDIUM:
            rate = BaseFareStrategy.MEDIUM_VEHICLE_RATE
        else:
            rate = BaseFareStrategy.LARGE_VEHICLE_RATE
        
        fare = fare + (rate * ticket.calculate_parking_duration())
        return fare


