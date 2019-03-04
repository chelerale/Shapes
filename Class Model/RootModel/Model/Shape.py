from typing import *
from RootModel.Model.DrawingContext import DrawingContext
from RootModel.Model.Point2D import Point2D

class Shape:
    self.__drawing_context : Optional[DrawingContext]
    self.__location_points : List[Point2D] = []

    @abstractmethod
    def draw(context : DrawingContext) -> NoReturn:
        raise NotImplementedError('Implement me')

    @abstractmethod
    def location() -> NoReturn:
        pass

    @abstractmethod
    def move(target_location: Point2D) -> NoReturn:
        pass