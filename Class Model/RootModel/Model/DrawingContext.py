from typing import *
from abc import ABC, abstractmethod

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DrawingContext():
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
