from abc import ABC, abstractmethod

class PricingStrategy(ABC):

    @property
    @abstractmethod
    def price(self) -> float:
        pass