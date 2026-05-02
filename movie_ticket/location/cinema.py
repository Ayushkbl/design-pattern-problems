from movie_ticket.location.room import Room

class Cinema:

    def __init__(self, name: str, location: str):
        self.__name: str = name
        self.__location: str = location
        self.__rooms: list[Room] = []
    
    def add_room(self, room: Room) -> None:
        self.__rooms.append(room)

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def location(self) -> str:
        return self.__location
    
    @property
    def rooms(self) -> list[Room]:
        return self.__rooms