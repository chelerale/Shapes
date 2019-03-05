from typing import *
from .Point2D import Point2D
from tkinter import Event
from .TkinterDrawingContext import TkinterDrawingContext
import operator
from functools import reduce


# Supported shape types
SHAPES = [x.lower() for x in ['Segment']]

# Description: (number of points to click, is right-click required)
POINTS_DESC = [(2, False)]

class ClickHandler:
    def __init__(self) -> None:
        self.__accumulated_points : List[Point2D] = []
        self.__description = dict(zip(SHAPES, POINTS_DESC))

    def left_click(self, event: Event) -> None:
        if not hasattr(event, 'x') and not hasattr(event, 'y'):
            raise TypeError('Unsupported event type')
        
        self.__accumulated_points.append(Point2D(event.x, event.y))
        
        if len(self.__accumulated_points) == self.__description['segment'][0]:
            TkinterDrawingContext().draw_segment(self.__flatten_points())
            self.clear()

    def right_click(self, event: Event) -> None:
        raise NotImplementedError('Not supported yet')

    def clear(self) -> None:
        self.__accumulated_points.clear()

    def __flatten_points(self) -> List[float]:
        return reduce(
            operator.concat,
            map(lambda x: x.get_coordinates(), self.__accumulated_points)
        )