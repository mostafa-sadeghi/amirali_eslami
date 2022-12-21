# numbers = [1, 3, 5, 7, 2]
# numbers.sort(reverse=True)
# print(numbers)

# new_numbers = sorted(numbers)
# print(new_numbers)
# new_numbers = sorted(numbers, reverse=True)
# print(new_numbers)

# def get_item(item):
#     return item[1]


# product_items = [('item1', 1000), ('product4', 2000), ('product3', 1500)]
# product_items.sort(key=get_item)
# print(product_items)
# output = sorted(product_items, key=get_item)
# print(output)
# lambda function
# product_items = [('item1', 1000), ('product4', 2000), ('product3', 1500)]
# product_items.sort(key=lambda product_items: product_items[1])
# print(product_items)

# map function

# product_items = [('item1', 1000), ('product4', 2000), ('product3', 1500)]
# prices = []
# for item in product_items:
#     prices.append(item[1])

# print(prices)


# with map function:
# output = map(lambda product_item: product_item[1], product_items)
# my_list = []
# for o in output:
#     my_list.append(o)
# print(my_list)
# my_list = list(output)
# print(my_list)


# filter function

# product_items = [('item1', 1000), ('product4', 2000), ('product3', 1500)]
# temp = filter(lambda product_item: product_item[1] > 1000, product_items)
# print(list(temp))


# list comprehension
# product_items = [('item1', 1000), ('product4', 2000), ('product3', 1500)]

# prices = [product[1] for product in product_items]
# print(prices)
# prices = list(map(lambda item: item[1], product_items))
# print(prices)
# result =  [product for product in product_items if product[1]>1000]
# print(result)

# zip function
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# [(1,'a'), (2,'b'),(3,'c')]
# z = list(zip(l1, l2))
# print(z)
# print(list(zip('456', l1, l2)))


# stack LIFO

# persons = []
# persons.append(1)
# persons.append(2)
# persons.append(3)
# while persons:
#     print(persons.pop())
# print(persons.pop())
# print(persons.pop())

# QUEUE FIFO
# persons = []
# persons.append(1)
# persons.append(2)
# persons.append(3)
# persons.append(4)

# while persons:
#     print(persons.pop(0))

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)

# queue.popleft()
# print(queue)

# from array import array
# a = array('i', [1, 2, 3])
# print(a)
# print(type(a))
# a.append(4)
# print(a)


# sth = {'a': 1, 'b': 2, 'c': 3}
# out = {i: val*2 for i, val in sth.items()}
# print(out)
# print(type(out))


# out = (i*2 for i in range(10))
# print(list(out))
# out = [i*2 for i in range(10_000)]
# print(list(out))

# from sys import getsizeof
# values = (i*2 for i in range(1000))
# print(getsizeof(values))
# values = [i*2 for i in range(1000)]
# print(getsizeof(values))


# numbers = [1, 2, 3, 4]
# print(numbers)
# print(*numbers)
# print(1, 2, 3, 4)

# values = list(range(10))
# print(values)
# values = [*range(10)]
# print(values)

# l1 = [1, 2]
# l2 = [13, 4]
# l = l1 + l2
# print(l)
# l = [*l1, *l2]
# print(l)

# f = {'id': 1,
#      'name': 'nikan'

#      }

# m = {'family': 'rezaei', 'age': 40}
# n = {**f, **m}
# print(n)

# handling exceptions:
# try:
#     age = int(input('enter your age> '))
# except ValueError:
#     print('error occured')
# else:
#     print('no exception occured')

# print('adadasda')

# try:
#     file = open("f.txt")
#     age = int(input('enter your age '))
#     x = 10/age
# except (ValueError, ZeroDivisionError, FileNotFoundError):
#     print('ValueError or ZeroDivisionError or FileNotFoundError')
# else:
#     print('ok')
# finally:
#     file.close()

# try:
#     with open("f.txt") as f:
#         pass
# except:
#     pass

# with open("f1.txt") as f1, open('f2.txt') as f2:
#     pass


# how to raise exception?
# def calc_xfactor(age):
#     if age <= 0:
#         raise ValueError("age is invalid")
#     return 10/age


# try:
#     calc_xfactor(-10)
# except:
#     print('balalal')
# calc_xfactor(-10)
from timeit import timeit

code1 = """
def calc_xfactor(age):
    if age <= 0:
        raise ValueError("age is invalid")
    return 10/age


try:
    calc_xfactor(-10)
except:
    print('balalal')
"""
# x = timeit(code1, number=10000)
# print(x)

code2 = """
def calc_xfactor(age):
    if age <= 0:
        return 0
    return 10/age


try:
    calc_xfactor(-10)
except:
    print('balalal')
"""

x = timeit(code2)
print(x)
