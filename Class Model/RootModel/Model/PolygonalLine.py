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
        segment = LineShape()
        segment.begin = point if len(self.__inner_segments) == 0 else self.__inner_segments[-1].end
        segment.end = point
        self.__inner_segments.append(segment)