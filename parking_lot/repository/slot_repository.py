from typing import Optional
from collections import Counter

from domain.parkingSlot import ParkingSlot
from domain.vehicle import Vehicle

class SlotRepository:

    def __init__(self) -> None:
        self._slots: dict[str, ParkingSlot] = dict()
    
    def save(self, slot: ParkingSlot) -> ParkingSlot:
        self._slots[slot.id] = slot
        return slot
    
    def find_by_id(self, slot_id: str) -> Optional[ParkingSlot]:
        return self._slots.get(slot_id)
    
    def find_available_slots(self, vehicle_type: Vehicle.VehicleType):
        return [
            slot 
            for slot in self._slots.values()
            if slot.slot_type == vehicle_type and not slot.occupied
        ]
    
    def allocate_slot(self, vehicle_type: Vehicle.VehicleType) -> Optional[ParkingSlot]:
        for slot in self._slots.values():
            if slot.slot_type == vehicle_type and not slot.occupied:
                slot.occupied = True
                return slot
        
        return None
    
    def release_slot(self, slot_id: str) -> None:
        slot = self._slots.get(slot_id)
        if slot:
            slot.occupied = False

    def get_slot_statistics(self) -> dict[Vehicle.VehicleType, int]:
        return Counter(slot.slot_type.value for slot in self._slots.values())
    
    def clear(self):
        self._slots.clear()