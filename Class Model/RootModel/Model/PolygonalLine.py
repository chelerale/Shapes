from typing import * 
from .LineShape import LineShape
from .DrawingContext import DrawingContext

class PolygonalLine:
    def __init__(self) -> None:
        self.__inner_segments : List[LineShape] = []

    def draw(context : DrawingContext) -> None:
        raise NotImplementedError('Implement me')