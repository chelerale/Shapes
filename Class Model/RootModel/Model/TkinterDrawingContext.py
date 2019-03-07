from .DrawingContext import DrawingContext, Singleton
from typing import *
from tkinter import Canvas


class TkinterDrawingContext(DrawingContext, metaclass=Singleton):

    def parameter_count_controller(count_param: int, err_msg: str):
        def decorator(func : Callable):
            def wrapper(self, params):
                if len(params) != count_param:
                    raise ValueError(
                        "Invalid parameter count in function {}, params got: {}, \
                        excepted count :{} ,tip : {}".format(
                            func, params, count_param, err_msg
                        )
                    )
                result = func(self, params)
                return result
            return wrapper
        return decorator


    def __init__(self, canvas: Canvas) -> None:
        if canvas is None:
            raise ValueError('None canvas provided')

        self.__canvas : Canvas = canvas
        super().__init__()

    def draw_arc(self, params : Tuple[int, ...]):
        raise NotImplementedError('Implement me')

    @parameter_count_controller(4, 'Top-left and bottom-right expected')
    def draw_ellipse(self, params : Tuple[int, ...]):
        x0, y0, x1, y1 = params
        self.__canvas.create_oval(x0, y0, x1, y1)

    @parameter_count_controller(2, '(x, y) exprected')
    def draw_point(self, params : Tuple[int, ...]):
        x, y, r = *params, 1
        self.__canvas.create_oval(x-r, y-r, x+r, y+r, width=2)

    @parameter_count_controller(4, 'Top-left (x, y) and right_bottom (x, y)')
    def draw_rectangle(self, params : Tuple[int, ...]):
        x0, y0, x1, y1 = params
        self.__canvas.create_rectangle(x0, y0, x1, y1)

    @parameter_count_controller(4, 'x0, y0, x1, y1')
    def draw_segment(self, params: Tuple[int, ...]):
        x0, y0, x1, y1 = params
        self.__canvas.create_line(x0, y0, x1, y1)

    def get_area_size(self):
        return self.__canvas.winfo_width(), self.__canvas.winfo_height()

    def set_color(self, color):
        raise NotImplementedError('Implement me')

    def set_line_style(self, style):
        raise NotImplementedError('Implement me')