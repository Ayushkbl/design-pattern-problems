from collections import defaultdict
from typing import Dict, List, Optional

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

    def get_seats_by_number(self, seat_number: str) -> Optional[Seat]:
        return self.__seats_by_number.get(seat_number)

    def get_seats_by_position(self, row: int, column: int) -> Optional[Seat]:
        row_seats = self.__seats_by_position.get(row)
        return row_seats.get(column) if row_seats else None
    
    def get_all_seats(self) -> List[Seat]:
        return list(self.__seats_by_number.values())
    
    

