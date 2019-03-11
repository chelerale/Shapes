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
    def draw_arc(self, params : Tuple[int, ...]):
        pass

    @abstractmethod
    def draw_ellipse(self, params : Tuple[int, ...]):
        pass
    
    @abstractmethod
    def draw_rhombus(self, params : Tuple[int, ...]):
        pass
    
    @abstractmethod
    def draw_parallelogram(self, params : Tuple[int, ...]):
        pass

    @abstractmethod
    def draw_point(self, params : Tuple[int, ...]):
        pass

    @abstractmethod
    def draw_rectangle(self, params : Tuple[int, ...]):
        pass

    @abstractmethod
    def draw_segment(self, params : Tuple[int, ...]):
        pass

    @abstractmethod
    def draw_polygonal_shape(self, params: Tuple[int, ...]):
        pass

    @abstractmethod
    def get_area_size(self):
        pass
