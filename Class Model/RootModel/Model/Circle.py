#######################################################
# 
# Circle.py
# Python implementation of the Class Circle
# Generated by Enterprise Architect
# Created on:      04-���-2019 0:36:43
# Original author: Lenovo-PC
# 
#######################################################
from .Ellipse import Ellipse
from .DrawingContext import DrawingContext


class Circle(Ellipse):
    def draw(self, context: DrawingContext):
        a, b, c, d = *self.begin.get_coordinates(), *self.end.get_coordinates()
        dx = a - c
        dy = b - d
        summ = dx * dx + dy * dy
        radius = pow(summ, 0.5)
        context.draw_ellipse((a - radius, b + radius, a + radius, b - radius))