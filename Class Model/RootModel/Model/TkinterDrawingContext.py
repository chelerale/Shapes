from RootModel.Model.DrawingContext import DrawingContext
from typing import *
from tkinter import Canvas

def parameter_count_controller(count_param: int, err_msg: str):
    def decorator(func : Callable):
        def wrapper(*args, **kwargs):
            if (len(args) != count_param):
                raise ValueError(
                    "Invalid parameter count in function {}, params got: {}, tip : {}".format(
                        func, args, err_msg
                    )
                )
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


class TkinterDrawingContext(DrawingContext):

    def __init__(self, canvas: Canvas) -> None:
        if canvas is None:
            raise ValueError('None canvas provided')

        self.__canvas : Canvas = canvas
        super().__init__()

    def draw_arc(params : Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    @parameter_count_controller(4, 'Top-left and bottom-right expected')
    def draw_ellipse(params : Tuple[float, ...]):
        x0, y0, x1, y0 = *params
        self.__canvas.create_oval(x0, y0, x1, y1)

    @parameter_count_controller(2, '(x, y) exprected')
    def draw_point(params : Tuple[float, ...]):
        x, y, r = *params, 1
        self.__canvas.create_oval(x-r, y-r, x+r, y+r, width=2)

    def draw_rectangle(Point : Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    def draw_segment(Point: Tuple[float, ...]):
        raise NotImplementedError('Implement me')

    def set_color(color):
        raise NotImplementedError('Implement me')

    def set_line_style(style):
        raise NotImplementedError('Implement me')