from typing import *
from abc import ABC, abstractmethod

class DrawingContext(ABC):

    def __init__(self):
        pass

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
