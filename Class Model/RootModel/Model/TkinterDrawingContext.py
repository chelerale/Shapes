from RootModel.Model.DrawingContext import DrawingContext
from typing import *
from tkinter import Canvas

def parameter_count_controller(count_param: int, err_msg: str):
    def decorator(func : Callable):
        def wrapper(*args, **kwargs):
            if (len(args) != count_param):
                raise ValueError(
                    "Invalid parameter count in function {}, params got: {}, \
                     excepted count :{} ,tip : {}".format(
                        func, args, count_param, err_msg
                    )
                )
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


class Singleton:
    _instance : DrawingContext = None
    
    def __call__(cls, *args, **kwargs):
        if not isinstance(cls, DrawingContext):
            raise AttributeError
        if self._instance is None:
            self._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return self._instance



class TkinterDrawingContext(DrawingContext):

    __metaclass__ = Singleton
    def __init__(self, canvas: Canvas) -> None:
        if canvas is None:
            raise ValueError('None canvas provided')

        self.__canvas : Canvas = canvas
        super().__init__()

    def draw_arc(params : Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    @parameter_count_controller(4, 'Top-left and bottom-right expected')
    def draw_ellipse(params : Tuple[float, ...]):
        x0, y0, x1, y1 = *params
        self.__canvas.create_oval(x0, y0, x1, y1)

    @parameter_count_controller(2, '(x, y) exprected')
    def draw_point(params : Tuple[float, ...]):
        x, y, r = *params, 1
        self.__canvas.create_oval(x-r, y-r, x+r, y+r, width=2)

    @parameter_count_controller(4, 'Top-left (x, y) and right_bottom (x, y)')
    def draw_rectangle(params : Tuple[float, ...]):
        x0, y0, x1, y1 = *params
        self.__canvas.create_rectangle(x0, y0, x1, y1)

    @parameter_count_controller(4, 'x0, y0, x1, y1')
    def draw_segment(Point: Tuple[float, ...]):
        x0, y0, x1, y1 = *params
        self.__canvas.create_line(x0, y0, x1, y1)

    def set_color(color):
        raise NotImplementedError('Implement me')

    def set_line_style(style):
        raise NotImplementedError('Implement me')