from typing import *
from RootModel.Model.Segment import Segment

class Ray(Segment):

    def draw(drawingContext) -> NoReturn:
        raise NotImplementedError('Implement me')

    def __get_last_point_intersection(self, bounds: Tuple[int, int]) -> NoReturn:
        raise NotImplementedError('Not implemented')