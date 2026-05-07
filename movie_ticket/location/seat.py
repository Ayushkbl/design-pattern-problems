from typing import Optional

from movie_ticket.rate.normal_rate import NormalRate
from movie_ticket.rate.pricing_strategy import PricingStrategy

class Seat:

    def __init__(self, seat_number: str, pricing_strategy: Optional[PricingStrategy]):
        self.__seat_number = seat_number
        self.__pricing_strategy = pricing_strategy
    
    @property
    def seat_number(self) -> str:
        return self.__seat_number
    
    @property
    def pricing_strategy(self) -> Optional[PricingStrategy]:
        return self.__pricing_strategy
    
    @pricing_strategy.setter
    def pricing_strategy(self, pricing_strategy: PricingStrategy) -> None:
        self.__pricing_strategy = pricing_strategy
    