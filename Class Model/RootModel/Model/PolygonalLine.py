from typing import * 
from .LineShape import LineShape
from .DrawingContext import DrawingContext
from .Point2D import Point2D


class PolygonalLine:
    def __init__(self) -> None:
        self.__inner_segments: List[LineShape] = []
        self.__last_segment : LineShape = None

    def draw(self, context: DrawingContext) -> None:
        if self.__last_segment is not None:
            self.__last_segment.draw(context)
            begin, end = self.__last_segment.begin, self.__last_segment.end

            context.draw_segment((*begin.get_coordinates(), *end.get_coordinates()))
            self.__last_segment = None
        
    def addPoint(self, point: Point2D) -> None:
        segment = LineShape()
        segment.begin = point if len(self.__inner_segments) == 0 else self.__inner_segments[-1].end
        segment.end = point
        self.__inner_segments.append(segment)
        self.__last_segment = segment