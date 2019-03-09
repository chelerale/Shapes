from typing import *
from .LineShape import LineShape
from .DrawingContext import DrawingContext


class Segment(LineShape):
    
    def draw(self, context: DrawingContext):
        a, b, c, d = *self.begin.get_coordinates(), *self.end.get_coordinates()
        context.draw_segment((a, b, c, d))