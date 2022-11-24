
# numbers = [str(item) for item in [1, 2, 3, 4]]
# print(numbers)


# def applyToEach(L, f) -> list:
#     for i in range(len(L)):
#         L[i] = f(L[i])
#     return L


# def f(s):
#     return str(s)


# x = applyToEach([1, 2, 3, 4, 5], f)
# print(x)

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()


# def my_func():
#     print("blalalalal")


# label = ttk.Button(root, text="hello...", command=my_func)
# label.pack()


# root.mainloop()


# def my_func():
#     pass


# x = my_func()

# print(x)
# print(my_func())


# List of functions


# def applyFuns(L, x):
#     for f in L:
#         print(f(x))


# applyFuns([min, max], [1, 2, 3, 4])

# map function

numbers = [1, -2, 3, -4]
# new_num= []
# for num in numbers:
#     new_num.append(abs(num))

# print(new_num)
# new_num = map(abs, numbers)
# print(type(new_num))
# for item in new_num:
#     print(item)


# numbers = [[1, 2, 3], [4, 5, 6]]
# new_num = map(max, numbers)
# for item in new_num:
#     print(item)


# l1 = [1, 2, 3]
# l2 = [0, 1, 5, 6]

# for item in map(min, l1, l2):
#     print(item)

# def custom_mul(x, y):
#     result = 0
#     while x > 0:
#         result += y
#         x -= 1
#     return result


# x = custom_mul(2, 2)
# print(x)

# custom_mul with recursion:
# def custom_mul(a, b):  # a=1 b=2
#     if a == 1:
#         return b
#     return b + custom_mul(a-1, b)  # 2 +  2 + 2


# x = custom_mul(2, 2)
# print(x)


# factorial with iteration

# def fact(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result


# result = fact(3)
# print(result)


# def outer():
#     def inner():
#         return "inner"
#     return inner()


# print(outer())


def isPalindromic(string):
    def toChars(string):
        string = string.lower()
        characters = ''
        for char in string:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                characters += char
        return characters

    def isPal(string):  # aba
        if len(string) <= 1:
            return True
        elif string[0] == string[-1] and isPal(string[1:-1]):
            return True
        else:
            return False
    return isPal(toChars(string))


x = isPalindromic('aba')
print(x)
