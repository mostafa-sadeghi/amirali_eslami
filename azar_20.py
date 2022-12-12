# array = [[1, 2, 3], [4, 5, 6]]
# print(array[0][0])
# print(array[1][1])

# array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# for i in range(len(array)):
#     for j in range(len(array[i])):
#         for k in range(len(array[i][j])):
#             print(array[i][j][k], end=' ')
# array.clear()
# print(array)
# array2 = array.copy()
# array.clear()

# print(array)
# print(array2)
# array = [1, 2, 3]
# a = [4, 5, 6]
# # print(array.count(1))
# array.extend(a)
# print(array)


# numbers = [1, 2, 1, 4]
# print(numbers.index(1))
# numbers.insert(2, 100)
# print(numbers)
# print(numbers.pop(2))
# print(numbers)
# numbers.remove(1)
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# new_numbers = sorted(numbers, reverse=True)
# print(new_numbers)


# def get_price(item):
#     return item[1]


# products = [('item1', 1000), ('item2', 3500), ('item3', 2000)]
# # products.sort()
# # print(products)
# new_products = sorted(products, key=get_price, reverse=True)
# print(new_products)


# def max_value(matrix):
#     m, n = len(matrix), len(matrix[0])
#     largets_item = matrix[0][0]
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] > largets_item:
#                 largets_item = matrix[i][j]
#     return largets_item


# result = max_value(array)
# print(result)

def show_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    result = '-'*28 + '\n'
    for i in range(m):
        result += '|'
        for j in range(n):
            result += f'{matrix[i][j]:>7}'

        result += '     |' + '\n'
    result += '-'*28
    return result


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
output = show_matrix(array)
# print(output)


def size(matrix):
    return (len(matrix), len(matrix[0]))


# print(size(array))


# def transpose(matrix):
#     m, n = size(matrix)
#     transpose_matrix = []
#     rows = [0]*m

#     for i in range(n):
#         transpose_matrix.append(rows)
#         rows = [0]*m

#     # another way with list comprehension
#     transpose_matrix = [[0]*m for i in range(n)]
#     for i in range(m):
#         for j in range(n):
#             transpose_matrix[j][i] = matrix[i][j]

#     print(transpose_matrix)
#     return transpose_matrix


# trans_mat = transpose(array)
# res = show_matrix(trans_mat)
# print(res)
array = [[1, 2, 3], [4222222, 5, 6], [1, 80, 90], [10, 11111, 12]]


def max_row(matrix):
    max_val = 0
    rows, cols = len(matrix), len(matrix[0])
    row_index = 0
    for row in range(rows):
        if sum(matrix[row]) > max_val:
            max_val = sum(matrix[row])
            row_index = row

    return row_index


print(max_row(array))
# def max_row(matrix):
#     max_val = matrix[0][0]
#     rows, cols = len(matrix), len(matrix[0])
#     row_index, col_index = (0, 0)
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col] > max_val:
#                 max_val = matrix[row][col]
#                 row_index = row
#                 col_index = col

#     return (row_index, col_index)


# print(max_row(array))
