from datetime import datetime
from typing import Optional

from parking_lot.vehicle.vehicle import Vehicle
from parking_lot.spot.parking_spot import ParkingSpot

class Ticket:

    def __init__(self, ticket_id: str, vehicle: Vehicle, parking_spot: ParkingSpot, entry_time: datetime):
        self._ticket_id: str = ticket_id
        self._vehicle: Vehicle = vehicle
        self._parking_spot: ParkingSpot = parking_spot
        self._entry_time: datetime = entry_time
        self._exit_time: Optional[datetime] = None
    
    # Getters and setters
    @property
    def ticket_id(self):
        return self._ticket_id

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def parking_spot(self):
        return self._parking_spot

    @property
    def entry_time(self):
        return self._entry_time
    
    @property
    def exit_time(self):
        return self._exit_time
    
    @exit_time.setter
    def exit_time(self, exit_time: datetime):
        self._exit_time = exit_time
    

    def calculate_parking_duration(self) -> float:
        exit_time = self._exit_time if self._exit_time else datetime.now()

        duration = exit_time - self._entry_time
        return (duration.seconds / 60)
