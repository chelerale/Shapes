from typing import *
from .Point2D import Point2D
from .Shape import Shape
from abc import abstractmethod
from .DrawingContext import DrawingContext

class LineShape(Shape):
    def __init__(self) -> None:
        self.__first : Optional[Point2D] = None
        self.__second : Optional[Point2D] = None
        super().__init__()

    @abstractmethod
    def draw(self, context : DrawingContext) -> None:
        pass

    @property
    def begin(self) -> Point2D:
        return self.__first
    
    @begin.setter
    def begin(self, value:Point2D) -> None:
        if value is None:
            raise ValueError('None point provided')
        self.__first = value

    @property
    def end(self) -> Point2D:
        return self.__second
    
    @end.setter
    def end(self, value:Point2D) -> None:
        if value is None:
            raise ValueError('None point provided')
        self.__second = value