from typing import *
from RootModel.Model.Point2D import Point2D
from RootModel.Model.Shape import Shape

class LineShape(Shape):
    self.__first : Optional[Point2D] = None
    self.__second : Optional[Point2D] = None

    @abstract
    def draw(context : DrawingContext) -> NoReturn:
        pass

    @property
    def begin(self) -> Point2D:
        return self.__first
    
    @begin.setter
    def begin(self, value:Point2D) -> NoReturn:
        if value is None:
            raise ValueError('None point provided')
        self.__first = value

    @property
    def end(self) -> Point2D:
        return self.__second
    
    @end.setter
    def end(self, value:Point2D) -> NoReturn:
        if value is None:
            raise ValueError('None point provided')
        self.__second = value