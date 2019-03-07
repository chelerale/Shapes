from typing import *
from .Segment import Segment

class Ray(Segment):

    def draw(self, drawingContext) -> None:
        raise NotImplementedError('Implement me')

    def __get_last_point_intersection(self, bounds: Tuple[int, int]) -> None:
        raise NotImplementedError('Not implemented')