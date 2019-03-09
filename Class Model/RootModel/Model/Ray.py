from typing import *
from .Segment import Segment
from .DrawingContext import DrawingContext

class Ray(Segment):

    def draw(self, context: DrawingContext) -> None:
        a, b, c, d = *self.begin.get_coordinates(), *self.end.get_coordinates()
        context.draw_segment((a, b, a + (c - a) * 1000, b + (d - b) * 1000))

    def __get_last_point_intersection(self, bounds: Tuple[int, int]) -> None:
        raise NotImplementedError('Not implemented')