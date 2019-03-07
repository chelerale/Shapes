from typing import *
from .DrawingContext import DrawingContext
from .Point2D import Point2D
from abc import abstractmethod

class Shape:
    def __init__(self) -> None:
        self.__location_points : List[Point2D] = []

    @abstractmethod
    def draw(self, context : DrawingContext) -> None:
        pass#raise NotImplementedError('Implement me')

    @abstractmethod
    def location(self) -> None:
        pass

    @abstractmethod
    def move(self, target_location: Point2D) -> None:
        pass