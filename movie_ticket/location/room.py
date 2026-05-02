from movie_ticket.location.layout import Layout

class Room:

    def __init__(self, room_number: str, layout: Layout) -> None:
        self.__room_number = room_number
        self.__layout = layout
    
    @property
    def room_number(self) -> str:
        return self.__room_number
    
    @property
    def layout(self) -> Layout:
        return self.__layout