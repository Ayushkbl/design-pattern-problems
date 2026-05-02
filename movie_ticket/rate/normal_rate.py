from movie_ticket.rate.pricing_strategy import PricingStrategy

class NormalRate(PricingStrategy):

    def __init__(self, price: float):
        self.__price: float = price
    
    @property
    def price(self) -> float:
        return self.__price