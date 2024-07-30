"""
    Bridge
        -a structural design pattern that lets you split a large class
        into two separate hierarchies - abstraction and implementation - which
        can be developed independently of each other.
"""
import abc


class Shape(abc.ABC):  # Abstraction
    def __init__(self, color) -> None:
        self.color = color

    def show(self):
        pass


class Circle(Shape):  # Refined Abstraction
    def show(self):
        self.color.paint('circle')


class Square(Shape):  # Refined Abstraction
    def show(self):
        self.color.paint('square')


class triangle(Shape):
    def show(self):
        self.color.paint('triangle')


class Color(abc.ABC):  # Implementation
    def paint(self, name):
        pass


class Blue(Color):  # Concrete Implementation
    def paint(self, name):
        print(f'this is a blue {name}')


class Red(Color):  # Concrete Implementation
    def paint(self, name):
        print(f'this is a red {name}')


class Yellow(Color):
    def paint(self, name):
        print(f'this is a yellow {name}')
