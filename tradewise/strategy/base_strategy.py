# base_strategy.py

from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    def __init__(self, stock_quotes, category="v40"):
        self.stock_quotes = stock_quotes
        self.category = category

    @abstractmethod
    def apply_strategy(self, *args, **kwargs):
        """
        Abstract method to apply the strategy.
        Subclasses must implement this method.
        """
        pass

