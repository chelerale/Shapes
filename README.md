# Shapes

# Запуск приложения 
Перейти в директорию, содержащую файл `main.py`, в командной строке ввести:
```
python3 main.py
```
Клики по поверхности для рисования перенаправляются в класс `ClickHandler` одноименного модуля. Для каждого типа поддерживаемой фигуры он хранит следующие параметры: `(points_required, right_click_required, handler_function)`.
Для внесения изменений редактировать `SHAPES_DESC`. Пример:
```python
"Ray" : (2, False, segment_accumulator)
"Polygonal Line" : (inf, True, poly_line_accumulator)
```
Здесь под `handler_function` понимается функция, передающая точку в модель либо сохраняющая ее внутри своего тела. Пример:
```python
def segment_accumulator(point: Point2D, segment: Segment, counter : int) -> None:
    if counter not in {0, 1}:
        raise ValueError('Invalid number of points in segment')

    if counter == 0:
        segment.begin = point
    else:
        segment.end = point
```
Метод отрисовки `draw` модели вызывается автоматически при наборе нужного количества точек или при нажатии правой кнопки.
Реализовать все модели, методы их отрисовки, а также способы передачи точек в модели.
Во всех моделях предусмотреть конструкторы `__init__` без параметров, точки передавать через `property`. Пример того, как написать `property`:
```python
@property
def begin(self) -> Point2D:
    return self.__first
    
@begin.setter
def begin(self, value:Point2D) -> None:
    if value is None:
        raise ValueError('None point provided')
    self.__first = value
```
Доступ осуществляется:
```python
point = Point2D()
var = point.begin
point.begin = some_point
```

