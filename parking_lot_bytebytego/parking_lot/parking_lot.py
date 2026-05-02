import uuid
from datetime import datetime

from parking_lot.fare.fare_calculator import FareCalculator
from parking_lot.vehicle.vehicle import Vehicle
from parking_lot.spot.parking_manager import ParkingManager
from parking_lot.fare.ticket import Ticket

class ParkingLot:

    def __init__(self, parking_manager: ParkingManager, fare_calculator: FareCalculator):
        self._parking_manager: ParkingManager = parking_manager
        self._fare_calculator: FareCalculator = fare_calculator
    
    # Method to handle vehicle entry into the parking lot
    def enter_vehicle(self, vehicle: Vehicle):
        spot = self._parking_manager.park_vehicle(vehicle)

        if spot:
            ticket = Ticket(self.generate_ticket_id(), vehicle, spot, datetime.now())
            return ticket
        
        return None

    # Method to handle vehicle exit from the parking lot
    def leave_vehicle(self, ticket: Ticket):

        if ticket and not ticket.exit_time:
            ticket.exit_time = datetime.now()
            self._parking_manager.unpark_vehicle(ticket.vehicle)
            fare = self._fare_calculator.calculate_fare(ticket)

    
    @staticmethod
    def generate_ticket_id():
        return f"TICKET-{uuid.uuid4()}"

