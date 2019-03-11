from typing import *
from .Point2D import Point2D
from .Shape import Shape
from abc import abstractmethod
from .DrawingContext import DrawingContext

from .Parallelogram import Parallelogram

class Rectangle(Parallelogram):
    def __init__(self) -> None:
        self.__rec_points: List[Point2D] = []
     
    def draw(self, context: DrawingContext) -> None:
        aX, aY = self.__rec_points[0].get_coordinates()
        bX, bY = self.__rec_points[1].get_coordinates()
        
        context.draw_polygonal_shape((aX, aY, aX, bY, bX, bY, bX, aY))
        
    def addPoint(self, point: Point2D) -> None:
        self.__rec_points.append(point)