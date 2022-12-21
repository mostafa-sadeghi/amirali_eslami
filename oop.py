# x = 1
# print(type(x))
# class Human:
#     name = ''
#     family = ''
#     age = ''

#     def speak(self):
#         print("speak")


# ali = Human()
# ali.name = 'ali'
# ali.family = 'rezaei'
# ali.speak()
# print(ali.name)
# h2 = Human()

# class Point:
#     color = 'green'

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print("draw")

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)


# point = Point.zero()
# p2 = Point(2, 2)
# p2.zero()
# print(p2.x)
# p2.__class__.color = "blue"
# print(point.color)
# print(Point.color)

# point = Point(1, 5)
# print(point.x)
# print(point.y)
# point.draw()
# point.z = 15

# another_point = Point(10, 12)
# print(point.color)
# print(another_point.color)
# print(Point.color)

# class level attributes


# point = Point()
# print(type(point))
# print(isinstance(point, Point))
# class MyClass:
#     def method(self):
#         return 'instance method called', self

#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls

#     @staticmethod
#     def staticmethod():
#         return 'static method called'


# obj = MyClass()
# print(obj.method())
# MyClass.method(obj)


# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'Pizza({self.ingredients!r})'


# p = Pizza(['cheese', 'tomatoes'])
# print(p)
# class Point:
#     color = 'green'

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print("draw")

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     def __eq__(self, o):
#         return self.x == o.x and self.y == o.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y+other.y)


# point1 = Point(1, 2)
# point2 = Point(1, 2)
# # print(point)
# # print(str(point))
# print(point1 == point2)

# print(point1 + point2)


# private member:
# class Point:
#     __color = "red"


# # print(Point.__color)
# print(Point.__dict__)
# print(Point._Point__color)

# class Point:
#     def __init__(self):
#         self.__color = "red"


# point = Point()
# # print(point.__dict__)
# print(point._Point__color)


# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, val):
#         if val < 0:
#             raise ValueError('Price can not be negative')
#         self.__price = val

# price = property(get_price, set_price)


# product = Product(50)
# product.price = 10
# print(product.price)


from abc import ABC, abstractclassmethod


class Animal:

    def __init__(self):
        self.age = 2
        print("Animal Constructor")

    def eat(self):
        print("eat")


class Mammal(Animal):

    def __init__(self):
        print("Mammal Constructor")
        super().__init__()
        self.weight = 15

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


# DRY
mammal = Mammal()
print(mammal.weight)
print(mammal.age)

# print(isinstance(mammal, Mammal))
# print(issubclass(Mammal, Animal))


# Multi level Inheritance

# class Bird(Animal):
#     def fly(self):
#         print("fly")


# class Chicken(Bird):
#     pass

# Multiple Inheritance

class Employee:
    def greet(self):
        print('Employee greet')


class Person:
    def greet(self):
        print('Person greet')


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


class Stream(ABC):
    def read()
