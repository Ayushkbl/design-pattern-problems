import uuid
from .vehicle import Vehicle

class PricingRule:
    """
    PricingRule Domain Model
    
    Defines the pricing for a specific vehicle type.
    """

    def __init__(self, vehicle_type: Vehicle.VehicleType, rate_per_hour: float, flat_rate: float) -> None:
        self.id: str = str(uuid.uuid4())
        self.vehicle_type: Vehicle.VehicleType = vehicle_type
        self.rate_per_hour: float = rate_per_hour
        self.flat_rate: float = flat_rate
    
    def update_rates(self, rate_per_hour: float, flat_rate: float) -> None:
        self.rate_per_hour = rate_per_hour
        self.flat_rate = flat_rate
    
    def __str__(self) -> str:
        return (f"PricingRule{{id={self.id}"
                f", vehicle_type = {self.vehicle_type.value}"
                f", rate_per_hour = {self.rate_per_hour}"
                f", flat_rate = {self.flat_rate}}}")