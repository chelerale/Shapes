from typing import *

class DrawingContext:
    @abstractmethod
    def draw_arc(params : Tuple[float, ...]):
        pass

    @abstractmethod
    def draw_ellipse(params : Tuple[float, ...]):
        pass

    @abstractmethod
    def draw_point(Point : Tuple[float, ...]):
        pass

    @abstractmethod
    def draw_rectangle(Point : Tuple[float, ...]):
        pass

    @abstractmethod
    def draw_segment(Point : Tuple[float, ...]):
        pass
