# x = 0


# def func():
#     global x
#     x += 1


# def func2():
#     global x
#     x += 2


# func()
# func2()
# print(x)


# def isPalindromic(string):

#     def toChars(string):
#         string = string.lower()
#         characters = ''
#         for char in string:
#             if char in 'abcdefghijklmnopqrstuvwxyz':
#                 characters += char
#         return characters

#     def isPal(string):  # aba
#         global numbCalls
#         numbCalls += 1
#         if len(string) <= 1:
#             return True
#         elif string[0] == string[-1] and isPal(string[1:-1]):
#             return True
#         else:
#             return False
#     return isPal(toChars(string))


# # print(__name__)
# numbCalls = 0
# if __name__ == "__main__":
#     isPalindromic("aabaa")
#     print("numCalls", numbCalls)
# import calendar
# # set firstweekday=0
# cal = calendar.Calendar()
# for x in cal.iterweekdays():
#     print(x)
# import calendar as cal
# print(cal.weekday(2022, 11, 26))
# print(cal.day_name[cal.weekday(2022, 11, 26)])

# import random
# import math
# import calendar

# f = open('file.txt', 'w')

# for i in range(2):
#     name = input('> ')
#     f.write(name + '\n')

# f.close()

# f = open('file.txt', 'r')

# for i in range(2):
#     print(f.read())

# f.close()

# with open('file.txt', 'r') as f:
#     for i in range(2):
#         print(f.read())
# with open('file.txt', 'a') as f:
#     for i in range(2):
#         name = input('> ')
#         f.write(name + '\n')

# print(2*'ss')
# print(2*['ss'])
# x = 'aaabc'
# x[0] = 'c' > error
# print('d' not in x)
# x = [1, 2, 3]
# y = [3, 2, 1]
# print(x == y)
# x = {1, 2, 3}
# y = {3, 2, 1, 1}
# print(x == y)
# print(x[1])
# x.add(6)
# print(x)
# x.discard(1)
# x.discard(7)
# x.remove(2)
# print(x)

student1 = {'name': 'anna', 'grade': 'B', 'course': 2}
student2 = {'name': 'bob', 'grade': 'A', 'course': 3}
student3 = {'name': 'john', 'grade': 'c', 'course': 2}
student1['age'] = 23
student2['age'] = 32
student3['age'] = 25
students = []
students.append(student1)
students.append(student2)
students.append(student3)
del students[0]['name']
# print(students)
print(students[0].keys())
for key in students[0].keys():
    print(key)
for val in students[0].values():
    print(val)
# print(students[0]['name'])
