from enum import Enum
import uuid

class Vehicle:

    class VehicleType(Enum):
        BIKE = "BIKE"
        CAR = "CAR"
        TRUCK = "TRUCK"
        EV = "EV"

    def __init__(self, license_plate: str, vehicle_type: VehicleType) -> None:
        self.id: str = str(uuid.uuid4())
        self.license_plate: str = license_plate
        self.vehicle_type: Vehicle.VehicleType = vehicle_type
    
    def __str__(self) -> str:
        return (f"Vehicle{{id={self.id}"
                f", license_plate = {self.license_plate}"
                f", vehicle_type = {self.vehicle_type.value}}}")