from abc import ABC, abstractmethod

from parking_lot.vehicle.vehicle import Vehicle
from parking_lot.vehicle.vehicle_size import VehicleSize

class ParkingSpot(ABC):

    @abstractmethod
    def is_available(self) -> bool:
        pass

    @abstractmethod
    def occupy(self, vehicle: Vehicle) -> None:
        pass

    @abstractmethod
    def vacate(self) -> None:
        pass

    @property
    @abstractmethod
    def spot_number(self) -> int:
        pass

    @property
    @abstractmethod
    def size(self) -> VehicleSize:
        pass