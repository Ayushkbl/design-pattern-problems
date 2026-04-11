import uuid
from datetime import datetime

class Ticket:
    """
    Ticket Domain Model
    
    Issued at vehicle entry. Tracks vehicle/slot association and entry time.
    """

    def __init__(self, vehicle_id: str, slot_id: str) -> None:
        self.id: str = str(uuid.uuid4())
        self.vehicle_id: str = vehicle_id
        self.slot_id: str = slot_id
        self.entry_time: datetime = datetime.now()
        self.active: bool = True
    
    def deactivate(self) -> None:
        self.active = False

    def __str__(self) -> str:
        return (f"Ticket{{id={self.id}"
                f"vehicle_id={self.vehicle_id}"
                f"slot_id={self.slot_id}"
                f"entry_time={self.entry_time}"
                f"is_active={self.is_active}}}")