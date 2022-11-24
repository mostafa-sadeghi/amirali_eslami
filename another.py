

# string = "aaaNme"


# def my_fuc(string):

#     my_list = []
#     for s in string:
#         if s.islower():
#             my_list.append(s.upper())
#         else:
#             my_list.append(s.lower())
#     output = ''.join(my_list)
#     print(output)


# my_fuc(string)


# def my_func(string):
#     count = 0
#     for s in string:
#         if s.isdecimal():
#             count += 1

#     return count


# print(my_func("12 aaas0df123"))


# def my_func(number):
#     total = 0
#     for n in number:
#         if n.isdecimal():
#             total = total + int(n)

#     return total


# print(my_func('----------12----34'))


# What is the average value of the digits in the number 3**(4**5)?
# Truncate your answer down to the nearest integer.

# For example, the number 235 has an average digit value of 3.33333,
# which, when truncated, is simply 3.

# def Question_9():
#     x = 3**(4**5)
#     print(x)
#     string = str(x)
#     total = 0
#     for s in string:
#         total += int(s)
#     return(round(total/len(string)))


# print(Question_9())

# What is the sum of the integers 1-10000 inclusive,
#  but leaving out numbers that are divisible by 3?


# def Question_10():
#     # numbers = [item for item in range(1, 10001) if item % 3 != 0]
#     numbers = []
#     for item in range(1, 10001):
#         if item % 3 != 0:
#             numbers.append(item)

#     return sum(numbers)


# print(Question_10())
#  Consider the numbers 59**(27**2) and 27**(31**2).
#  How many corresponding digits do these numbers have in common?
# For example, the numbers 123456 and 1486 have two digits in common,
# the 6 in the ones place and the 4 in the 100s place
# def numbers(a, b):
#     counter = 0
#     x = str(a)
#     y = str(b)
#     dif = len(x) - len(y)
#     if dif > 0:
#         y = y.zfill(dif + len(y))
#         print(y)
#     else:
#         pass
#         # // todo

#     for i in range(len(x)):
#         if x[i] == y[i]:
#             counter += 1

#     return counter


# print(numbers(59**(27**2), 27**(31**2)))


# number = int(input("enter number > "))

# for answer in range(0, number + 1):
#     if answer ** 3 >= number:
#         break

# if answer ** 3 == number:
#     print(answer)


# def my(string):
# first_char = string[0]
# string = string.replace(first_char, '#')
# return first_char + string[1:]
#     string = list(string)
#     for i in range(1, len(string)):

#         if string[0] == string[i]:
#             string[i] = "$"
#     print("".join(string))


# print(my("restart"))
