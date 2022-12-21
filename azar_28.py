# x = 1
# print(type(x))
from abc import ABC, abstractmethod


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('speak')

    def __str__(self):
        return self.name


h1 = Human('ali', 30)
# print(h1)
# print(h1.age)
# h1.family = "balalal"
# print(h1.family)
# h2 = Human('reza', 23)
# print(h2.age)


# class Point:
#     __color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(self.x)

#     @classmethod
#     def zero(cls):

#         return cls(0, 0)

#     def change_color_(self):
#         self.color = "black"

#     @classmethod
#     def change_color(cls):
#         cls.color = "green"

#     def __str__(self):
#         return f'({self.x},{self.y})'

#     def __repr__(self):
#         return f'({self.x},{self.y})'

#     def __eq__(self, o):
#         return self.x == o.x and self.y == o.y


# print(Point._Point__color)

# p1 = Point(1, 2)
# p2 = Point(1, 2)
# # print(str(p))
# # print(p)
# print(p1 == p2)

# print(Point.change_color())
# print(Point.color)


# point = Point.zero()
# print(point.x)

# p1 = Point(1, 2)
# p2 = Point(13, 32)
# p3 = Point(3, 23)
# p1.change_color_()
# print(p1.color)
# print(p2.color)
# print(p3.color)
# print(Point.color)


# class Product:
#     def __init__(self, price):
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError('some thing')
#         self.__price = value


# product = Product(-100)
# print(product.price)


# product._Product__price = 100
# print(product._Product__price)


# abstract base class


# class Stream(ABC):
#     @abstractmethod
#     def read(self):
#         pass


# class MemoryStream(Stream):
#     def read(self):
#         print('memory')


# class IOStream(Stream):
#     def read(self):
#         print('io')


# polymorphism


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("textbox")


class CheckBox(UIControl):
    def draw(self):
        print('checkbox')


def draw(controls):
    for control in controls:
        control.draw()


# textbox = TextBox()
# checkbox = CheckBox()
# draw([textbox, checkbox])


class TextBox:
    def draw(self):
        print('textbox')


class CheckBox:
    def draw(self):
        print('checkbox')


def draw(controls):
    for control in controls:
        control.draw()


textbox = TextBox()
print(dir(textbox))
# checkbox = CheckBox()
# draw([textbox, checkbox])
