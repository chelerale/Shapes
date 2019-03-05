from typing import *

class Point2D:
    def __init__(self, x:float, y:float):
        self.__x, self.__y = x, y
        
    def get_coordinates(self) -> Tuple[float, float]:
        return self.__x, self.__y

    def set_coordinates(self, x : float, y : float) -> None:
        self.__x, self.__y = x, y