# import array

# x = array.array('i', [1, 2, 3, 4])
# # x = [1, 2, 3, 4]
# print(type(x))
# print(x)

# import numpy as np

# a = np.array([1, 2, 3])
# print(a[0])


# matrix = [[1, 2, 3], [4, 5, 6], [0, 2, 4], [2, 3, 4]]


# def largest_val(matrix):
#     m, n = len(matrix), len(matrix[0])
#     largest = matrix[0][0]
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] > largest:
#                 largest = matrix[i][j]
#     return f'largest element is {largest}'


# print(largest_val(matrix))

def printmx(matrix):
    for row in matrix:
        for col in row:
            print(f'{col:>4}', end=' ')
        print()


# printmx(matrix)
def size(mx):
    m, n = len(mx), len(mx[0])
    return m, n


# print(size(matrix))

matrix = [[1, 2, 3], [4, 5, 6], [0, 2, 4], [2, 3, 4]]


def transpose(matrix):
    m, n = size(matrix)
    print(m, n)
    other = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            other[i][j] = matrix[j][i]
    return other


output = transpose(matrix)
printmx(output)


def maxrow(matrix):
    max_ = 0
    max_row = []

    for row in matrix:
        if sum(row) > max_:
            max_ = sum(row)
            max_row = row

    return max_, max_row


print(maxrow(matrix))
