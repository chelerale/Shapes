from typing import *
from .Point2D import Point2D
from tkinter import Event
from .Segment import Segment
from .TkinterDrawingContext import TkinterDrawingContext
import operator
from functools import reduce


def segment_accumulator(point: Point2D, segment: Segment, counter : int) -> None:
    if counter not in {0, 1}:
        raise ValueError('Invalid number of points in segment')

    if counter == 0:
        segment.begin = point
    else:
        segment.end = point


# Supported shape types
SHAPES = [x.lower() for x in ['Segment']]

# Description: (number of points to click, is right-click required)
POINTS_DESC = [(2, False, segment_accumulator)]

# Classes
OBJECTS = [Segment]

# 
FACTORY = dict(zip(SHAPES, OBJECTS))


class ClickHandler:
    def __init__(self) -> None:
        self.__accumulated_points : List[Point2D] = []
        self.__description = dict(zip(SHAPES, POINTS_DESC))
        self.__counter : int = 0
        self.__current_object : Shape = None
        self.__current_object_name : str = None

    def left_click(self, event: Event) -> None:
        if not hasattr(event, 'x') and not hasattr(event, 'y'):
            raise TypeError('Unsupported event type')
        
        if self.__current_object is None or self.__current_object_name is None:
            raise ValueError('None object to draw') 

        self.__description[self.__current_object_name][2](
            Point2D(event.x, event.y),
            self.__current_object,
            self.__counter
        )

        if self.__counter == self.__description[self.__current_object_name][0] - 1:
            self.__counter = 0
            self.__current_object.draw(TkinterDrawingContext())
            self.__recreate_object()
        else:
            self.__counter += 1
            
    def set_object(self, name: str) -> None:
        if name.lower() not in SHAPES:
            raise LookupError("Shape {} not found".format(name.lower()))
        self.__current_object_name = name.lower()
        self.__recreate_object()
        
    def __recreate_object(self) -> None:
        if self.__current_object_name is None or self.__current_object_name not in SHAPES:
            raise LookupError("Shape {} not found".format(self.__current_object_name))

        self.__current_object = FACTORY[self.__current_object_name]()

    def right_click(self, event: Event) -> None:
        raise NotImplementedError('Not supported yet')
