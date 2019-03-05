from RootModel.Model.DrawingContext import DrawingContext
from typing import *
from tkinter import Canvas

class TkinterDrawingContext(DrawingContext):

    def __init__(self, canvas: Canvas) -> None:
        if canvas is None:
            raise ValueError('None canvas provided')

        self.__canvas = canvas
        super().__init__()

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