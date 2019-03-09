from .Ray import Ray
from .DrawingContext import DrawingContext
from .Point2D import Point2D


class Line(Ray):

    def draw(self, context: DrawingContext) -> None:
        a, b, c, d = *self.begin.get_coordinates(), *self.end.get_coordinates()
        context.draw_segment((a - (c-a)*1000, b - (d - b)*1000, c, d))
        context.draw_segment((a, b, a + (c-a)*1000, b + (d-b)*1000))