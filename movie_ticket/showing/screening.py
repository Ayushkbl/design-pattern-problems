from datetime import datetime, timedelta

from movie_ticket.location.room import Room
from movie_ticket.showing.movie import Movie

class Screening:

    def __init__(self, movie: Movie, room: Room, start_time: datetime, end_time: datetime):
        self.__movie = movie
        self.__room = room
        self.__start_time = start_time
        self.__end_time = end_time
    
    def movie(self) -> Movie:
        return self.__movie
    
    def room(self) -> Room:
        return self.__room
    
    def start_time(self) -> datetime:
        return self.__start_time
    
    def end_time(self) -> datetime:
        return self.__end_time
    
    def duration(self) -> timedelta:
        return self.__end_time - self.__start_time