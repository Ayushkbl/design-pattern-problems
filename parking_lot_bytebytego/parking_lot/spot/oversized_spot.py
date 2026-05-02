from typing import Optional

from parking_lot.spot.parking_spot import ParkingSpot
from parking_lot.vehicle.vehicle import Vehicle
from parking_lot.vehicle.vehicle_size import VehicleSize

class OversizedSpot(ParkingSpot):

    def __init__(self, spot_number: int) -> None:
        self._spot_number: int = spot_number
        self._vehicle: Optional[Vehicle] = None
        self._size = VehicleSize.LARGE
    
    def is_available(self) -> bool:
        return False if self._vehicle else True

    def occupy(self, vehicle: Vehicle) -> None:
        if self.is_available():
            self._vehicle = vehicle

    def vacate(self) -> None:
        self._vehicle = None

    @property
    def spot_number(self) -> int:
        return self._spot_number

    @property
    def size(self) -> VehicleSize:
        return self._size