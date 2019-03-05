from typing import *
from .Point2D import Point2D
from tkinter import Event


class ClickHandler:
    def __init__(self) -> None:
        self.__accumulated_points : List[Point2D] = []

    def left_click(self, event: Event) -> None:
        if not hasattr(event, 'x') and not hasattr(event, 'y'):
            raise TypeError('Unsupported event type')

        self.__accumulated_points.append(Point2D(event.x, event.y))

    def right_click(self, event: Event) -> None:
        raise NotImplementedError('Not supported yet')

    def clear(self) -> None:
        self.__accumulated_points.clear()