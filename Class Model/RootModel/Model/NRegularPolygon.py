from .PolygonalShape import PolygonalShape
from math import sin, cos, pi
from .DrawingContext import DrawingContext
from .Point2D import Point2D


def rotate(x, y, angle_rad):
    c, s = cos(angle_rad), sin(angle_rad)
    return x * c + y * s, -x*s + y * c

class NRegularPolygon(PolygonalShape):
    def draw(self, context: DrawingContext):
        centre, edge = super().location_points[0], super().location_points[1]
        centre_x, centre_y = centre.get_coordinates()
        edge_x, edge_y = edge.get_coordinates()
        rot_angle = 2 * pi / self.__vertex_count
        print('Angle = {},cente = ({},{})'.format(rot_angle, centre_x, centre_y))
        super().location_points.clear()
        for i in range(self.__vertex_count):
            x, y = rotate(edge_x - centre_x, edge_y - centre_y, rot_angle * i)
            point = Point2D(x + centre_x, y + centre_y)
            super().addPoint(point, i == self.__vertex_count - 1)
        super().draw(context)

    def set_vertex_count(self, vertex_count: int):
        self.__vertex_count = vertex_count
        
    def addPoint(self, point, is_final):
        super().location_points.append(point)



