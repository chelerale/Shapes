from .Ray import Ray
from .DrawingContext import DrawingContext


class Line(Ray):
    def draw(context : DrawingContext) -> None :
        raise NotImplementedError('Implement me')