from parking_lot.vehicle.vehicle import Vehicle
from parking_lot.vehicle.vehicle_size import VehicleSize

class Car(Vehicle):

    def __init__(self, license_plate: str) -> None:
        self._license_plate = license_plate
        self._vehicle_size = VehicleSize.MEDIUM
    
    def get_license_plate(self) -> str:
        return self._license_plate

    @property
    def vehicle_size(self) -> VehicleSize:
        return self._vehicle_size