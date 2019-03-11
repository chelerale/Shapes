from typing import *
from .Point2D import Point2D
from .Shape import Shape
from abc import abstractmethod
from .DrawingContext import DrawingContext

from .PolygonalShape import PolygonalShape

class Parallelogram(PolygonalShape):
    def __init__(self) -> None:
        self.__points_list: List[Point2D] = []

    def draw(self, context: DrawingContext) -> None:
        aX, aY = self.__points_list[0].get_coordinates()
        bX, bY = self.__points_list[1].get_coordinates()
        cX, cY = self.__points_list[2].get_coordinates()
        
        dX = aX + (cX - bX);
        dY = cY + (aY - bY); 
       
        context.draw_polygonal_shape((aX, aY, bX, bY, cX, cY, dX, dY))
        
    def addPoint(self, point: Point2D) -> None:
        self.__points_list.append(point)