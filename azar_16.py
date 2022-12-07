# _s_1:int = 0
# def fun(x:int)->bool:
#     return True
# x = 1
# print(1,end='-')

# x = 1
# y = 2
# y = x # 1
# x = y
# print(x, y)

# x = 1
# y = 2

# temp = x
# x = y
# y = temp

# print(x, y)

# x = 1
# y = 2

# x,y = y,x
# print(x,y)


# l1 = [1,2]
# l2 = [3,4]
# l = l1 + l2
# print(l)

# x = input('> ')
# y = int(x)
# import math
# z = 1.2
# print(math.floor(z))
# z = round(1.4)
# print(z)


# number = int(float(input('> ')))
# print(number)

# x = [1, 2, 3]
# for item in x:
#     print(item)


# for i in range(len(x)):
#     print(x[i])

# x = [1, 2, 3]

# for x in enumerate(x):
#     print(x)
# for i, val in enumerate(x):
#     print(f'{i}th value is {val}')

# x = [1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]

# x1, *others, xlast = x
# print(x1, xlast)


# i = 0
# while i < len(x):
#     print(x[i])
#     i += 1

# numbers = []
# while True:
#     print('''
#     to exit -> 0,
#     to enter a number -> 1,
#     to search anumber -> 2,
#     to show all numbers -> 3,
#     to delete a number -> 4
#     ''')
#     entry = input('> ')
#     if entry == '0':
#         exit()
#     elif entry == '1':
#         while True:
#             x = input('enter a to add number | r to return> ')
#             if x == 'a':

#                 number = float(input('enter a number> '))
#                 numbers.append(number)
#             elif x == 'r':
#                 break
#     elif entry == '2':
#         x = float(input('enter a number to search> '))
#         if x in numbers:
#             print(f'{x} exists!!')
#             continue
#     elif entry == '3':
#         string = '-'.join([str(i) for i in numbers])
#         print(f'all numbers are {string}')
#         continue
#     elif entry == '4':
#         x = float(input('enter a number to del> '))
#         numbers.remove(x)
#         continue

# x = 'a'
# y = 'b'
# print(ord(x))
# print(ord(y))
# print(x > y)

s = 'hello'
print(id(s))
s = 'y' + s[1:]
print(id(s))
