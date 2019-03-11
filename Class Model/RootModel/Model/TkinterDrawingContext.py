from .DrawingContext import DrawingContext, Singleton
from typing import *
from tkinter import Canvas


class TkinterDrawingContext(DrawingContext, metaclass=Singleton, ):

    def parameter_count_controller(count_param: int, err_msg: str):
        def decorator(func: Callable):
            def wrapper(self, params, ):
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
            
        self.__canvas: Canvas = canvas
        self.__fill = 'white'
        self.__line = 'black'
        super().__init__()

    def draw_arc(self, params: Tuple[int, ...]):
        raise NotImplementedError('Implement me')

    @parameter_count_controller(4, 'Top-left and bottom-right expected')
    def draw_ellipse(self, params: Tuple[int, ...]):
        x0, y0, x1, y1 = params
        self.__canvas.create_oval(x0, y0, x1, y1, fill=self.__fill)

    @parameter_count_controller(2, '(x, y) exprected')
    def draw_point(self, params: Tuple[int, ...]):
        x, y, r = *params, 2
        self.__canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.__fill)

    @parameter_count_controller(4, 'Top-left (x, y) and right_bottom (x, y)')
    def draw_rectangle(self, params: Tuple[int, ...]):
        self.__canvas.create_polygon(*params, fill=self.__fill, outline=self.__line)
    
    @parameter_count_controller(4, 'Top-left (x, y) and right_bottom (x, y)')
    def draw_rhombus(self, params: Tuple[int, ...]):
        self.__canvas.create_polygon(*params, fill=self.__fill, outline=self.__line)
                
    @parameter_count_controller(6, 'Top-left (x, y) and right_bottom (x, y)')
    def draw_parallelogram(self, params: Tuple[int, ...]):
        self.__canvas.create_polygon(*params, fill=self.__fill, outline=self.__line)

    @parameter_count_controller(4, 'x0, y0, x1, y1')
    def draw_segment(self, params: Tuple[int, ...]):
        x0, y0, x1, y1 = params
        self.__canvas.create_line(x0, y0, x1, y1)

    def draw_polygonal_shape(self, params: Tuple[int, ...]):
        self.__canvas.create_polygon(*params, fill=self.__fill, outline=self.__line)

    def get_area_size(self):
        return self.__canvas.winfo_width(), self.__canvas.winfo_height()

    def set_color(self, color):
        raise NotImplementedError('Implement me')

    def set_line_style(self, style):
        raise NotImplementedError('Implement me')
