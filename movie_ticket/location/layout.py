from collections import defaultdict
from typing import Dict, List

from movie_ticket.location.seat import Seat

class Layout:

    def __init__(self, rows: int, columns: int) -> None:
        self.__rows: int = rows
        self.__columns: int = columns
        self.__seats_by_number: Dict[str, Seat] = dict()
        self.__seats_by_position: Dict[int, Dict[int, Seat]] = defaultdict(dict)
        self.__initialize_layout()
    
    def __initialize_layout(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                seat_number = f"{i}-{j}"
                self.add_seat(seat_number, i, j, Seat(seat_number, None))
    
    def add_seat(self, seat_number: str, row: int, column: int, seat: Seat):
        self.__seats_by_number[seat_number] = seat
        self.__seats_by_position[row][column] = seat

    @property
    def seats_by_number(self) -> Dict[str, Seat]:
        return self.__seats_by_number

    @property
    def seats_by_position(self) -> Dict[int, Dict[int, Seat]]:
        return self.__seats_by_position
    
    @property
    def all_seats(self) -> List[Seat]:
        return list(self.__seats_by_number.values())
    
    

