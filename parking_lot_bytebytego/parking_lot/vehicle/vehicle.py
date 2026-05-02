from abc import ABC, abstractmethod
from parking_lot.vehicle.vehicle_size import VehicleSize

class Vehicle(ABC):

    @abstractmethod
    def get_license_plate(self) -> str:
        pass

    @property
    @abstractmethod
    def vehicle_size(self) -> VehicleSize:
        pass
