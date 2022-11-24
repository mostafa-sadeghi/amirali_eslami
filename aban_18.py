# length = 2
# string = 'abc'

# print(len(string))
# snake case :
# my_string = ''
# camel case:
# myString = ''

# upper case:
# PI = 3.14

# upper camel case:
# MyString = 2
# MyString /= 3

# print(MyString)


# factorial function recursive

# def factorail(number):
# if type(number) == int:
# if isinstance(number, int) and number >= 0:
#     if number == 1:
#         return 1
#     return number * factorail(number-1)

# else:
#     print("some thing else")
# another way:
#     return 1 if (number == 1 or number == 0) else number * factorail(number-1)


# try:
#     print(factorail(0))
# except RecursionError:
#     print("some thing")


def find_sym_numbers():
    numbers = []
    for i in range(100, 1000):
        if str(i) == str(i)[::-1]:
            numbers.append(i)
    return len(numbers), numbers


print(find_sym_numbers())

# x = 123
# y = str(x)
# z = y[::-1]
# print(z)

# def reverse(string):
#     my_list = []
#     for i in range(len(string)-1, -1, -1):
#         my_list.append(string[i])
#     return "".join(my_list)

# print(reverse('321'))
