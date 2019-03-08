from typing import * 
from .LineShape import LineShape
from .DrawingContext import DrawingContext
from .Point2D import Point2D


class PolygonalLine:
    def __init__(self) -> None:
        self.__inner_segments: List[LineShape] = []

    segment = property()

    def draw(self, context: DrawingContext) -> None:
        for segment in self.__inner_segments:
            context.draw_segment((segment.begin.get_coordinates(), segment.end.get_coordinates()))
    # raise NotImplementedError('Implement me')

    @segment.setter
    def segment(self, segment: LineShape) -> None:
        self.__inner_segments.append(segment)

    def addPoint(self, point: Point2D) -> None:
        if len(self.__inner_segments) == 0:
            segment = LineShape()
            segment.begin = point
            segment.end = point
            self.__inner_segments.append(segment)
        else:
            segment = LineShape()
            firstPoint = self.__inner_segments[-1].end
            segment.begin = firstPoint
            segment.end = point
            self.__inner_segments.append(segment)