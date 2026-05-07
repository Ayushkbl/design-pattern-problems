from typing import List, Optional

from movie_ticket.location.cinema import Cinema
from movie_ticket.location.seat import Seat
from movie_ticket.showing.movie import Movie
from movie_ticket.showing.screening import Screening
from movie_ticket.ticket.screening_manager import ScreeningManager
from movie_ticket.ticket.ticket import Ticket


class MovieBookingSystem:

    def __init__(self):
        self.__movies: List[Movie] = list()
        self.__cinemas: List[Cinema] = list()
        self.__screening_manager = ScreeningManager()
    
    def add_movie(self, movie: Movie) -> None:
        self.__movies.append(movie)
    
    def add_cinema(self, cinema: Cinema) -> None:
        self.__cinemas.append(cinema)
    
    @property
    def movies(self) -> List[Movie]:
        return self.__movies
    
    @property
    def cinemas(self) -> List[Cinema]:
        return self.__cinemas
    
    @property
    def screening_manager(self) -> ScreeningManager:
        return self.__screening_manager
    
    def get_screening_for_movies(self, movie: Movie) -> List[Screening]:
        return self.__screening_manager.get_screenings_for_movie(movie)

    def get_tickets_for_screening(self, screening: Screening) -> List[Ticket]:
        return self.__screening_manager.get_tickets_for_screening(screening)
    
    def get_available_seats(self, screening: Screening) -> List[Seat]:
        return self.__screening_manager.get_available_seats(screening)
    
    def add_screening(self, movie: Movie, screening: Screening) -> None:
        self.__screening_manager.add_screening(movie, screening)
    
    def get_ticket_count(self, screening: Screening) -> int:
        return len(self.__screening_manager.get_tickets_for_screening(screening))
    
    def book_ticket(self, screening: Screening, seat: Seat):
        price = seat.pricing_strategy.price if seat.pricing_strategy else 0
        ticket = Ticket(screening, seat, price)
        self.__screening_manager.add_tickets(screening, ticket)