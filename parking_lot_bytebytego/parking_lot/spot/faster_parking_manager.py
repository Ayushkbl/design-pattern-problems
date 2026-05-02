from typing import Dict, Optional

from parking_lot.vehicle.vehicle_size import VehicleSize
from parking_lot.spot.parking_spot import ParkingSpot
from parking_lot.vehicle.vehicle import Vehicle

class ParkingManager:

    def __init__(self, available_spots: Dict[VehicleSize, list[ParkingSpot]]):
        self._available_spots: Dict[VehicleSize, list[ParkingSpot]] = available_spots
        self._vehicle_to_spot_map: Dict[Vehicle, ParkingSpot] = dict()
        self._spot_to_vehicle_map: Dict[ParkingSpot, Vehicle] = dict()
    
    def find_spot_for_vehicle(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        vehicle_size = vehicle.vehicle_size

        # Start looking for the smallest spot that can fit the vehicle
        for size in VehicleSize:
            if size.value >= vehicle_size.value:
                spots = self._available_spots.get(size, [])
                for spot in spots:
                    if spot.is_available():
                        return spot
        
        return None

    def park_vehicle(self, vehicle: Vehicle):
        spot = self.find_spot_for_vehicle(vehicle)

        if spot:
            spot.occupy(vehicle) # Occupy the Parking spot with the vehicle
            self._vehicle_to_spot_map[vehicle] = spot # Record the parking spot for the vehicle
            self._spot_to_vehicle_map[spot] = vehicle
            self._available_spots.get(spot.size, []).remove(spot) # Remove the spot from the available list
            return spot # Parking successful
        
        return None # No spot found for this vehicle
    
    def unpark_vehicle(self, vehicle: Vehicle):
        spot = self._vehicle_to_spot_map.pop(vehicle, None)
        if spot:
            self._spot_to_vehicle_map.pop(spot)
            spot.vacate()
            self._available_spots.get(spot.size, []).append(spot)
    
    # Used for Testing
    def find_vehicle_by_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        return self._vehicle_to_spot_map.get(vehicle)

    def find_spot_by_vehicle(self, spot: ParkingSpot) -> Optional[Vehicle]:
        return self._spot_to_vehicle_map.get(spot)