from typing import Dict, Optional

from parking_lot.vehicle.vehicle import VehicleSize
from parking_lot.spot.parking_spot import ParkingSpot
from parking_lot.spot.regular_spot import RegularSpot
from parking_lot.spot.parking_manager import ParkingManager
from parking_lot.fare.fare_strategy import FareStrategy
from parking_lot.fare.base_fare_strategy import BaseFareStrategy
from parking_lot.fare.peak_hours_fare_strategy import PeakHoursFareStrategy
from parking_lot.fare.fare_calculator import FareCalculator
from parking_lot.fare.ticket import Ticket
from parking_lot.parking_lot import ParkingLot
from parking_lot.vehicle.vehicle import Vehicle
from parking_lot.vehicle.Car import Car

class TestParkingLot:

    def test_vehicle_journey(self):
        print("\n=== Testing Parking Lot System: Complete Vehicle Journey ===")
        print("\n--- Setting Up Parking Spots ---")
        available_spots: Dict[VehicleSize, list[ParkingSpot]] = dict()
        available_spots[VehicleSize.MEDIUM] = []
        available_spots[VehicleSize.MEDIUM].append(RegularSpot(1))
        available_spots[VehicleSize.MEDIUM].append(RegularSpot(2))
        print("✓ Created 2 regular parking spots for medium-sized vehicles")
        print("  - Spot 1: Regular parking spot")
        print("  - Spot 2: Regular parking spot")

        print("\n--- Initializing Parking Manager ---")
        parking_manager: ParkingManager = ParkingManager(available_spots)
        print("✓ Parking manager initialized with available spots")

        print("\n--- Setting Up Fare Calculation System ---")
        strategies: list[FareStrategy] = [BaseFareStrategy(), PeakHoursFareStrategy()]
        fare_calculator: FareCalculator = FareCalculator(strategies)
        print("✓ Fare calculator initialized with multiple strategies:")
        print("  - Base fare strategy")
        print("  - Peak hours fare strategy")

        parking_lot: ParkingLot = ParkingLot(parking_manager, fare_calculator)
        
        print("\n--- Creating Test Vehicle ---")
        car: Vehicle = Car("ABC123")
        print("✓ Created car with license plate: ABC123")
        print("  - Vehicle type: Car (MEDIUM size)")

        print("\n--- Vehicle Entering Parking Lot ---")
        #  Vehicle enters the parking lot
        ticket: Optional[Ticket] = parking_lot.enter_vehicle(car)
        print("✓ Ticket generated for vehicle ABC123")
        assert ticket != None, "Ticket should not be null"
        if ticket:
            print(f"✓ Parking spot assigned: {ticket.parking_spot.spot_number}")
        assert car == ticket.vehicle, "Vehicle should match the one that entered"
        assert ticket.parking_spot != None, "Parking spot should not be null"
        print("✓ Ticket validation passed:")
        print("  - Ticket is not null")
        print("  - Vehicle matches the one that entered")
        print("  - Parking spot assigned successfully")

        #  Find the vehicle in the parking lot
        found_spot: Optional[ParkingSpot] = parking_manager.find_vehicle_spot(car)
        assert found_spot != None, "Vehicle should be found in the parking lot"
        assert ticket.parking_spot == found_spot, "Found spot should match the ticket's spot"
        
        print("\n--- Vehicle Leaving Parking Lot ---")
        #  Vehicle leaves the parking lot
        parking_lot.leave_vehicle(ticket)
        assert ticket.exit_time != None, "Exit time should be set"
        assert found_spot.is_available() == True, "Parking spot should be available after vehicle leaves"
        print("✓ Vehicle exit verification passed:")
        print("  - Exit time recorded on ticket")
        print("  - Parking spot is now available for other vehicles")
        print("=== Parking Lot Vehicle Journey Test Completed Successfully ===\n")