from tkinter import *
from typing import *
from Model.TkinterDrawingContext import TkinterDrawingContext
from Model.ClickHandler import ClickHandler, SHAPES_DESC


class ApplicationWindow:
    __WINDOW_SIZE: Tuple[int, int] = (600, 600)

    def __init__(self, master) -> None:
        if master is None:
            raise ValueError('Master is None')

        self.__master = master
        self.__master.title('Shape drawer')
        self.__master.geometry('x'.join(str(x) for x in self.__WINDOW_SIZE))
        self.__clicker: ClickHandler = ClickHandler()

        self.__create_menu()

        self.__canvas: Canvas = Canvas(
            self.__master,
            width=self.__WINDOW_SIZE[0],
            height=self.__WINDOW_SIZE[1]
        )
        self.__setup_canvas()
        
    def __create_menu(self) -> None:
        menubar = Menu(self.__master)
        self.__master.config(menu=menubar)

        shapes_menu = Menu(menubar)
        menubar.add_cascade(label='Shapes', menu=shapes_menu)
        self.__create_shapes_menu(shapes_menu)

        vis_menu = Menu(menubar)
        menubar.add_cascade(label='Visual', menu=vis_menu)
        self.__create_visual_repr_menu(vis_menu)

    def __create_shapes_menu(self, shapes_menu: Menu) -> None:
        for label in SHAPES_DESC.keys():
            shapes_menu.add_command(
                label=label,
                command=lambda x=label: self.__clicker.set_object(x)
            )

        self.__clicker.set_object('Segment')

    def __create_visual_repr_menu(self, vis_menu: Menu) -> None:
        vis_menu.add_command(label='Line Color', command=None)
        vis_menu.add_command(label='Line Style', command=None)
        vis_menu.add_command(label='Fill Color', command=None)

    def __setup_canvas(self) -> None:
        self.__canvas.bind("<Button 1>", lambda e: self.__clicker.left_click(e))
        self.__canvas.bind("<Button 3>", lambda e: self.__clicker.right_click(e))
        self.__canvas.pack(fill=BOTH, expand=YES)
        TkinterDrawingContext(self.__canvas)


if __name__ == '__main__':
    root = Tk()
    app = ApplicationWindow(root)

    root.mainloop()
