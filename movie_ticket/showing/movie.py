from datetime import timedelta

class Movie:

    def __init__(self, title: str, genre: str, duration_in_minutes: int):
        self.__title = title
        self.__genre = genre
        self.__duration_in_minutes = duration_in_minutes
    
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def genre(self) -> str:
        return self.__genre
    
    @property
    def duration_in_minutes(self) -> timedelta:
        return timedelta(minutes = self.__duration_in_minutes)