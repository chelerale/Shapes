from typing import *
from .DrawingContext import DrawingContext
from .Point2D import Point2D
from abc import abstractmethod


class Shape:
    def __init__(self) -> None:
        self._location_points : List[Point2D] = []

    @abstractmethod
    def draw(self, context : DrawingContext) -> None:
        pass#raise NotImplementedError('Implement me')

    @abstractmethod
    def location(self) -> None:
        pass

    @property
    def location_points(self) -> List[Point2D]:
        return self._location_points

    @abstractmethod
    def move(self, target_location: Point2D) -> None:
        pass