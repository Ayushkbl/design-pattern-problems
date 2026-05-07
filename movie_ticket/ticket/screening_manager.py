from typing import Dict, List, Optional
from collections import defaultdict

from movie_ticket.location.seat import Seat
from movie_ticket.showing.movie import Movie
from movie_ticket.showing.screening import Screening
from movie_ticket.ticket.ticket import Ticket

class ScreeningManager:

    def __init__(self) -> None:
        self.__screenings_by_movie: Dict[Movie, List[Screening]] = defaultdict(list)
        self.__tickets_by_screening: Dict[Screening, List[Ticket]] = defaultdict(list)
    
    def add_screening(self, movie: Movie, screening: Screening) -> None:
        self.__screenings_by_movie[movie].append(screening)
    
    def get_screenings_for_movie(self, movie: Movie) -> List[Screening]:
        return self.__screenings_by_movie[movie]
    
    def add_tickets(self, screening: Screening, ticket: Ticket) -> None:
        self.__tickets_by_screening[screening].append(ticket)

    def get_tickets_for_screening(self, screening: Screening) -> List[Ticket]:
        return self.__tickets_by_screening[screening]
    
    def get_available_seats(self, screening: Screening) -> List[Seat]:

        all_seats = list(screening.room.layout.get_all_seats())
        booked_tickets = self.get_tickets_for_screening(screening)

        available_seats = list(all_seats)
        for ticket in booked_tickets:
            available_seats.remove(ticket.seat)
        
        return available_seats