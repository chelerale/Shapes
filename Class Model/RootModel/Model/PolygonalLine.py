from typing import * 
from RootModel.Model.LineShape import LineShape

class PolygonalLine:
    self.__inner_segments : List[LineShape] = []

    def draw(context : DrawingContext) -> NoReturn:
        raise NotImplementedError('Implement me')