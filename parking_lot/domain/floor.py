import uuid

from .parkingSlot import ParkingSlot
from .vehicle import Vehicle

class Floor:
    """
    Floor Domain Model
    
    Represents a floor in the parking lot containing multiple slots.
    """

    def __init__(self, floor_number: int) -> None:
        self.id: str = str(uuid.uuid4())
        self.floor_number: int = floor_number
        self.slots: list[ParkingSlot] = []
    
    def add_slot(self, slot: ParkingSlot) -> None:
        self.slots.append(slot)

    def get_available_slots(self, vehicle_type: Vehicle.VehicleType) -> list[ParkingSlot]:
        return [s for s in self.slots if s.slot_type == vehicle_type and not s.occupied]
    
    def get_available_slots_count(self, vehicleType) -> int:
        return len(self.get_available_slots(vehicleType))
    
    def __str__(self) -> str:
        return (f"Floor{{id={self.id}, "
                f"floor_number={self.floor_number}, "
                f"total_slots={len(self.slots)}}}")
