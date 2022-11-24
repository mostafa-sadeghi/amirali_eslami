# Q1

# strings_list = []


# def Q1():
#     for i in range(5):
#         string = input(f'Enter string {i+1}/5 > ')
#         strings_list.append(string)

#     for i in range(4, -1, -1):
#         print(f"string {i+1}/5:", strings_list[i])


# Q1()


# Q2
# def max(l):
#     float_list = []
#     for item in l:
#         # if type(item) == float:
#         # another way
#         # print(isinstance(item, float))
#         if isinstance(item, float):
#             float_list.append(item)

#     if len(float_list) == 0:
#         return None
#     float_list.sort()
#     return float_list[-1]


# print(max([1, 2, 'ali', 1.3, 1.6, 1.2]))

# Q3:
# def longest(l):
#     longest = ''
#     for string in l:
#         if len(string) > len(longest):
#             longest = string
#     return longest


# print(longest(['a', 'aaaaaaa', 'aa', '']))

# def longest(l):
#     string_list = []
#     for string in l:
#         string_list.append((len(string), string))
#     new_list = sorted(string_list, key=lambda string_list: string_list[0])
#     return new_list[-1][1]


# print(longest(['a', 'aaaaaaa', 'aa', '']))


# Q4:
# numbers_list = list(range(1, 101))
# print(numbers_list)
# numbers_tuple = tuple(range(1, 101))
# print(numbers_tuple)

# numbers_list = []

# for i in range(1, 101):
#     numbers_list.append(i)

# numbers_tuple = tuple(numbers_list)

# print('numbers list is : ', numbers_list)
# print('numbers tuple is : ', numbers_tuple)

# numbers_list = []
# print('first_list', id(numbers_list))
# numbers_tuple = ()
# print('first', id(numbers_tuple))

# for i in range(1, 2):
#     print(f'{i}_list', id(numbers_list))
#     numbers_list.append(i)
#     numbers_tuple += (i,)
#     print(i, id(numbers_tuple))

# n = (1, 2, 3, 4)
# n2 = (5, 6, 7)
# print(n + n2)


# Q6
# import math


# def distance(a, b):
#     return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


# print(distance((1, 2), (3, 4)))

# def perimeter(points):
#     result = 0
#     for i in range(len(points)-1):
#         result += distance(points[i], points[i+1])
#     else:
#         result += distance(points[0], points[i+1])
#     return result

# another way
# def perimeter(points):
#     result = 0
#     for i in range(len(points)-1):
#         result += distance(points[i], points[i+1])
#     result += distance(points[0], points[-1])
#     return result


# print(perimeter([(1, 2), (3, 4), (5, 6), (7, 8)]))

# Q7
import random


def permutation(l):
    p = []
    c = list(l)
    for i in range(len(c)):
        i = random.randrange(0, len(c))
        p.append(c.pop(i))
    return p


print(permutation([1, 2, 3, 4]))
print(permutation(range(0, 30)))
print(permutation([1, 2, 3, 4]))
print(permutation(range(0, 30)))
print(permutation([19, 4, 3, 17]))
print(permutation([19, 4, 3, 17]))
print(permutation([(0, 0), (20, 0), (20, 10), (0, 10)]))
print(permutation([(0, 0), (20, 0), (20, 10), (0, 10)]))
my_list = [19, 4, 3, 17]
print(random.sample(my_list, len(my_list)))
print(random.sample(my_list, len(my_list)))
