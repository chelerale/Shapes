from typing import *
from .Point2D import Point2D
from tkinter import Event
from .Segment import Segment
from .PolygonalShape import PolygonalShape
from .Line import Line
from .Ray import Ray
from .Circle import Circle
from .Rectangle import Rectangle
from .Rhombus import Rhombus
from .Ellipse import Ellipse
from .Shape import Shape
from .Rectangle import Rectangle
from .Parallelogram import Parallelogram
from .PolygonalLine import PolygonalLine
from .NRegularPolygon import NRegularPolygon
from .TkinterDrawingContext import TkinterDrawingContext
import tkinter.simpledialog as simpledialog
import operator
from functools import reduce
from math import inf


def segment_accumulator(point: Point2D, segment: Segment, counter: int) -> None:
    if counter not in {0, 1}:
        raise ValueError('Invalid number of points in segment')

    if counter == 0:
        segment.begin = point
    else:
        segment.end = point


def polygon_accumulator(
        point: Point2D, poly: PolygonalShape,
        counter: int, right_click=False) -> None:
    poly.addPoint(point, right_click)
    poly.draw(TkinterDrawingContext())


def poly_line_accumulator(
        point: Point2D, poly: PolygonalLine,
        counter: int, right_click=False) -> None:
    if right_click:
        return

    poly.addPoint(point)
    poly.draw(TkinterDrawingContext())

def ellipse_accumulator(point: Point2D, ellipse: Ellipse, counter: int) -> None:
    if counter not in {0, 1}:
        raise ValueError('Invalid number of points in ellipse')

    if counter == 0:
        ellipse.begin = point
    else:
        ellipse.end = point

def circle_accumulator(point: Point2D, circle: Circle, counter: int) -> None:
    if counter not in {0, 1}:
        raise ValueError('Invalid number of points in circle')

    if counter == 0:
        circle.begin = point
    else:
        circle.end = point

def regular_polygon_accumulator(point: Point2D, poly: NRegularPolygon, counter: int) -> None:
    if counter not in {0, 1}:
        raise ValueError('Invalid number of points in regulat polygon')
    
    poly.addPoint(point, counter==1)
    if counter == 0:
        poly.set_vertex_count(REG_POLY_COUNT)
    

REG_POLY_COUNT = None
# Description: (number of points to click, is right-click required)
SHAPES_DESC = {
    "Segment": (2, False, segment_accumulator),
    "Line": (2, False, segment_accumulator),
    "Ray": (2, False, segment_accumulator),
    "Polygonal Line": (inf, True, poly_line_accumulator),
    "Polygon": (inf, True, polygon_accumulator),
    "Regular Polygon": (2, False, regular_polygon_accumulator),
    "Parallelogram": (2, False, None),
    "Rectangle": (2, False, None),
    "Rhombus": (2, False, None),
    "Ellipse": (2, False, ellipse_accumulator),
    "Circle": (2, False, circle_accumulator)
}

SHAPES_DESC = {
    k.lower(): v for k, v in SHAPES_DESC.items()
}

FACTORY = {
    "Segment": Segment,
    "Line": Line,
    "Ray": Ray,
    "Polygonal Line": PolygonalLine,
    "Polygon": PolygonalShape,
    "Regular Polygon": NRegularPolygon,
    "Parallelogram": Parallelogram,
    "Rectangle": Rectangle,
    "Rhombus": Rhombus,
    "Ellipse": Ellipse,
    "Circle": Circle
}

FACTORY = {
    k.lower(): v for k, v in FACTORY.items()
}


class ClickHandler:
    def __init__(self) -> None:
        self.__accumulated_points: List[Point2D] = []
        self.__counter: int = 0
        self.__current_object: Shape = None
        self.__current_object_name: str = None

    def left_click(self, event: Event) -> None:
        if not hasattr(event, 'x') and not hasattr(event, 'y'):
            raise TypeError('Unsupported event type')

        if self.__current_object is None or self.__current_object_name is None:
            raise ValueError('None object to draw')

        SHAPES_DESC[self.__current_object_name][2](
            Point2D(event.x, event.y),
            self.__current_object,
            self.__counter
        )

        if self.__counter == SHAPES_DESC[self.__current_object_name][0] - 1:
            self.__counter = 0
            self.__current_object.draw(TkinterDrawingContext())
            self.__recreate_object()
        else:
            self.__counter += 1

    def set_object(self, name: str) -> None:
        if name.lower() not in SHAPES_DESC:
            raise LookupError("Shape {} not found".format(name.lower()))

        if name.lower() == 'regular polygon':
            global REG_POLY_COUNT
            REG_POLY_COUNT = simpledialog.askinteger("Input", "Vertex count",
                                 minvalue=3, maxvalue=100)

        self.__current_object_name = name.lower()
        self.__recreate_object()

    def __recreate_object(self) -> None:
        if self.__current_object_name is None or self.__current_object_name not in SHAPES_DESC:
            raise LookupError("Shape {} not found".format(self.__current_object_name))

        self.__current_object = FACTORY[self.__current_object_name]()

    def right_click(self, event: Event) -> None:
        if self.__current_object_name not in SHAPES_DESC:
            raise ValueError('Unknown figure "{}"'.format(self.__current_object_name))

        if not SHAPES_DESC[self.__current_object_name][1]:
            return

        SHAPES_DESC[self.__current_object_name][2](
            Point2D(event.x, event.y),
            self.__current_object,
            self.__counter,
            True
        )

        self.__counter = 0
        self.__current_object.draw(TkinterDrawingContext())
        self.__recreate_object()
