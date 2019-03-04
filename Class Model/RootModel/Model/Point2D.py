from typing import *

class Point2D:
    self.__x : float
    self.__y : float

    def get_coordinates() -> Tuple[float, float]:
        return self.__x, self.__y

    def set_coordinates(self, x : float, y : float) -> NoReturn:
        self.__x, self.__y = x, y