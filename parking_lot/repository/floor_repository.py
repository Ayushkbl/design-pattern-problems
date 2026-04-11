from domain.floor import Floor
from uuid import UUID
from typing import Optional

class FloorRepository:

    def __init__(self) -> None:
        self._floors: dict[str,Floor] = dict()
        self._floor_number_to_id: dict[int, str] = dict()
    
    def save(self, floor: Floor) -> Floor:
        self._floors[floor.id] = floor
        self._floor_number_to_id[floor.floor_number] = floor.id
        return floor
    
    def find_by_id(self, floor_id: str) -> Optional[Floor]:
        return self._floors.get(floor_id, None)
    
    def find_by_number(self, floor_number: int) -> Optional[Floor]:
        return self._floors.get(self._floor_number_to_id.get(floor_number))
    
    def find_all(self) -> list[Floor]:
        return list(self._floors.values())
    
    def exists_by_number(self, floor_number: int) -> bool:
        return floor_number in self._floor_number_to_id
    
    def delete(self, floor_id: str) -> None:
        floor: Optional[Floor] = self._floors.pop(floor_id, None)
        if floor is not None:
            self._floor_number_to_id.pop(floor.floor_number, None)
    
    def clear(self):
        self._floors.clear()
        self._floor_number_to_id.clear()
