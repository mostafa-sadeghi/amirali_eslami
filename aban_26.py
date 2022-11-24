# import random


# def roll_dice(number):
#     dices = []
#     for i in range(number):
#         die = random.randrange(1, 7)
#         dices.append(str(die))
#     return dices


# dices = roll_dice(20)
# print(dices)


# def create_string(dices):

#     word_digits = "".join(dices)
#     count = 0
#     start = 0
#     output = []
#     for i in range(len(word_digits)-1):
#         if word_digits[i] == word_digits[i+1]:  # count: 0      i:0     start: 0
#             count += 1
#         else:
#             if start == count:
#                 output.append(f'{word_digits[start:count+1]}')
#             else:
#                 output.append(f'({" ".join(word_digits[start:count+1])})')
#             start = count + 1
#             count += 1
#     else:
#         if start == count:
#             output.append(f'{word_digits[start:count+1]}')
#         else:
#             output.append(f'({" ".join(word_digits[start:count+1])})')

#     return " ".join(output)


# print(create_string(dices))


# import random


# def roll_dice(number):
#     dices = []
#     for i in range(number):
#         die = random.randrange(1, 7)
#         dices.append(str(die))
#     return dices


# dices = roll_dice(20)
# # print(dices)


# def biggest_sequence(l):
#     bigest = ''
#     index = 0
#     for i in range(len(l)):
#         if len(l[i]) > len(bigest):
#             bigest = l[i]
#             index = i
#     return (index, bigest)


# def create_string(dices):

#     word_digits = "".join(dices)
#     count = 0
#     start = 0
#     output = []
#     for i in range(len(word_digits)-1):
#         if word_digits[i] == word_digits[i+1]:  # count: 0      i:0     start: 0
#             count += 1
#         else:

#             output.append(f'{" ".join(word_digits[start:count+1])}')
#             start = count + 1
#             count += 1
#     else:
#         output.append(f'{" ".join(word_digits[start:count+1])}')

#     index, bigest = biggest_sequence(output)
#     output[index] = f'({bigest})'
#     return " ".join(output)


# print(create_string(dices))

l = [False, False, True, False, False, False, False, True, True, False, False]


def largest_sequence(l):
    max_distance = 0
    largest_item = ()
    for item in l:
        if item[1]-item[0] > max_distance:
            max_distance = item[1]-item[0]
            largest_item = item
    return largest_item


def longestFalse(l):
    count = 0
    start = 0
    output = []
    for i in range(len(l)-1):  # count:1  start:2   i:2
        if l[i] == l[i+1]:
            count += 1
        else:
            output.append((start, count))
            start = count + 1
            count += 1
    else:
        output.append((start, count))

    largest_item = largest_sequence(output)

    return largest_item


print(longestFalse(l))
