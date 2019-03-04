from RootModel.Model.DrawingContext import DrawingContext
from typing import *

class QTDrawingContext(DrawingContext):
    def draw_arc(params : Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    def draw_ellipse(params : Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    def draw_point(Point : Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    def draw_rectangle(Point : Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    def draw_segment(Point: Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    def set_color(color):
        raise NotImplementedError('Implement me')

    def set_line_style(style):
        raise NotImplementedError('Implement me')