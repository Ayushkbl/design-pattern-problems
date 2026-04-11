import uuid

from .vehicle import Vehicle

class ParkingSlot:
    """
    ParkingSlot Domain Model
    
    Represents a single parking slot on a specific floor.
    """

    def __init__(self, slot_type: Vehicle.VehicleType, floor_number: int) -> None:
        self.id: str = str(uuid.uuid4())
        self.slot_type: Vehicle.VehicleType = slot_type
        self.occupied: bool = False
        self.floor_number: int = floor_number
    
    def __str__(self) -> str:
        return (f"ParkingSlot{{id={self.id}"
                f"slot_type={self.slot_type.value}"
                f"is_occupied={self.occupied}"
                f"floor_number={self.floor_number}}}")

