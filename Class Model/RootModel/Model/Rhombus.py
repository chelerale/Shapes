from typing import *
from .Point2D import Point2D
from .Shape import Shape
from abc import abstractmethod
from .DrawingContext import DrawingContext

from .Parallelogram import Parallelogram

class Rhombus(Parallelogram):
    def __init__(self) -> None:
        self.__points_list: List[Point2D] = []

    def draw(self, context: DrawingContext) -> None:
        aX, aY = self.__points_list[0].get_coordinates()
        bX, bY = self.__points_list[1].get_coordinates()
        
        context.draw_polygonal_shape((aX, bY, bX, 2 * bY - aY, 2 * bX - aX, bY, bX, aY))
    
    def addPoint(self, point: Point2D) -> None:
        self.__points_list.append(point)