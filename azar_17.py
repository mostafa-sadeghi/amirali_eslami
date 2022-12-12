# x = 25
# epsilon = 0.01
# numG = 0
# low = 1
# high = x

# g = (low + high)//2

# while abs(g**2 - x) >= epsilon:
#     numG += 1
#     if g**2 < x:
#         low = g
#     else:
#         high = g
#     g = (low + high)//2
# print('numGuesses', numG)
# print('answer', g)


# def to_binary(n):
#     is_neg = False
#     result = ''
#     if n < 0:
#         is_neg = True
#     if n == 0:
#         return '0'
#     while n > 0:
#         result = str(n % 2) + result
#         n = n // 2

#     if is_neg:
#         result = '-' + result

#     return result


# print(to_binary(4))

# print(3.2 % 1)

# x = float(input('enter a number> '))
# p = 0

# while (2**p * x) % 1 != 0:
#     print(f'reminder is : {(2**p * x) - int(2**p * x)}')
#     p += 1
# num = int(2**p * x)
# result = ''
# if num == 0:
#     result = '0'
# else:
#     while num > 0:

#         result = str(num % 2) + result
#         num = num // 2

# print(p)
# print(len(result))
# for i in range(p - len(result)):
#     result = '0' + result

# result = result[:-p] + '.' + result[-p:]
# print(result)

# print((0.1 + 0.2) == 0.3)

# epsilon = 0.01
# y = 24.0
# g = y/2
# ng = 0

# while abs(g**2 - y) >= epsilon:
#     ng += 1
#     g = g - (((g**2) - y)/(2*g))
# print(ng)
# print(g)

def my_func(x: int) -> int:
    '''
    This Function is use for sth
    Parameters:
    x:int
    Returns:int
    '''
    pass


my_func(1)
