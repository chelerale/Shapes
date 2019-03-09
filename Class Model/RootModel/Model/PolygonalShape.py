from .DrawingContext import DrawingContext
from .Point2D import Point2D
from .Shape import Shape
from .PolygonalLine import PolygonalLine

class PolygonalShape(Shape):

    def __init__(self):
        self.__is_last_final = False
        self.__last_point = None
        super().__init__()

    def addPoint(self, point: Point2D, is_final: bool) -> None:
        self.__is_last_final = is_final
        self.__last_point = point
        super().location_points.append(point)

    def draw(self, context: DrawingContext) -> None:
        if not self.__is_last_final:
            if self.__last_point is not None:
                context.draw_point(self.__last_point.get_coordinates())
        else:
            point_list = [x for p in super().location_points for x in p.get_coordinates() ]
            context.draw_polygonal_shape(point_list)
