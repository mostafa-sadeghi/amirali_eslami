

# print('''
#  to exit -> 0
#  to add number -> 1
#  to show sum -> 2

# ''')

# numbers = []
# while True:
#     entry = input("enter your choice-> ")
#     if entry == "0":
#         exit()
#     elif entry == '1':
#         while True:
#             number = input("enter number or show to show the result ")
#             if number == 'show':
#                 print(
#                     f'sum of {len(numbers)} numbers is equal to : {sum(numbers)}')
#                 exit()
#             numbers.append(int(number))
#     else:
#         print(f'bye')


# name = "amirali"
# family = "asdasdas"

# message = "hello %s %s" % (name, family)
# print(message)

# name = 'amirali'
# for ch in range(1, len(name), 2):
#     print(name[ch])


# for i in range(0, 1001, 2):
#     print(f'{i} is even number')


# numbers = list(range(0, 1001, 2))
# print(numbers)


# import math
# numbers = list(range(100))

# for i in numbers:
#     print(i)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1  # i = i + 1


# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)
#     if number == 3:
#         break

# else:
#     print("end")


# for number in numbers:
#     print(number)


# print("end")


# print('*' * 3)


# numbers = int(input("how many stars do you want? "))

# for num in range(3):
#     print('*', end='')

# print(math.ceil(2.2))
# x = []
# x = None
# print(bool(x))

# x = "" and "reza"
# print(x)


# numbers = [1, 2, 3, 4, 5]

# new_list = numbers[0:2:]

# print(new_list)

# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# numbers[0] = [1, "ali", [1, 2, 3]]
# print(numbers)
# n = int(input("enter number> "))

# for i in range(n, -1, -1):
#     print((i+1) * '*')

# numbers = [1, 2, 3, 5]
# print(numbers[-1])
# > >= < <= == !=

# print("bag" == "apple")
# print(ord("a"))
# print(ord("b"))

# age = 22
# if age >= 18:
#     message = "ok"
# else:
#     message = "not ok"
# print(message)

# message = "ok" if age >= 18 else "not ok"
# print(message)


# if "bag" > "cat" and "ali" == "ali":
#     print(True)
# if "ali" == "ali"  or "bag" > "cat":
#     print(True)
# if age >= 20 and age <=30:


# if 20 <= age <= 30:


# success = False

# for number in range(3):
#     print("attempt")


#     if success:
#         print("success")
#         break
# else:
#     print("attempted 3 times and faild")


# def my_func(name, family):
#     print(f"hello {name} {family}")


# my_func("ali")

# num_1 = int(input("enter number one > "))
# num_2 = int(input("enter number two > "))
# num_3 = int(input("enter number three > "))


# def maximum(num_1, num_2, num_3):
#     '''
#     This function is used to calculate the max number between inpu nums
#     Parameters :
#     Returns : int
#     '''
#     max_num = 0

#     if num_1 > max_num:
#         max_num = num_1
#     if num_2 > max_num:
#         max_num = num_2
#     if num_3 > max_num:
#         max_num = num_3

#     return f'max number between {num_1} {num_2} {num_3} is : {max_num}'


# print(maximum(num_1, num_2, num_3))


# max = 3
# print(max(1, 2, 3))

# import random
# frequency_1 = 0
# frequency_2 = 0
# frequency_3 = 0
# frequency_4 = 0
# frequency_5 = 0
# frequency_6 = 0

# for i in range(6_000_000):

#     face = random.randrange(1, 7)

#     if face == 1:
#         frequency_1 += 1
#     elif face == 2:
#         frequency_2 += 1
#     elif face == 3:
#         frequency_3 += 1
#     elif face == 4:
#         frequency_4 += 1
#     elif face == 5:
#         frequency_5 += 1
#     elif face == 6:
#         frequency_6 += 1

# print(f'Face{"Frequency":>14}')
# print(f'{1:>4}{frequency_1:>14}')
# print(f'{2:>4}{frequency_2:>14}')
# print(f'{3:>4}{frequency_3:>14}')
# print(f'{4:>4}{frequency_4:>14}')
# print(f'{5:>4}{frequency_5:>14}')
# print(f'{6:>4}{frequency_6:>14}')


# x, y = 2, 3
# x, y = y, x
# print('x: ', x)
# print('y: ', y)

# def my_func():
#     return 1


# print(my_func() == 1)

# def increment(number, by=1):
#     pass


# print(increment(2))


# import random


# def roll_dice():
#     die1 = random.randrange(1, 7)
#     die2 = random.randrange(1, 7)
#     return (die1, die2)


# def display_dice(dice):
#     die1, die2 = dice
#     print(f'player rolled {die1} + {die2} = {sum(dice)}')


# die_values = roll_dice()
# display_dice(die_values)

# sum_of_dice = sum(die_values)

# if sum_of_dice in (7, 11):
#     game_status = 'WON'
# elif sum_of_dice in (2, 3, 12):
#     game_status = "LOSE"
# else:
#     game_status = "CONTINUE"
#     my_point = sum_of_dice
#     print('Point is : ', my_point)

# while game_status == "CONTINUE":
#     die_values = roll_dice()
#     display_dice(die_values)
#     sum_of_dice = sum(die_values)

#     if sum_of_dice == my_point:
#         game_status = "WON"
#     elif sum_of_dice == 7:
#         game_status = "LOSE"

# if game_status == "WON":
#     print('player won')
# else:
#     print('you lose!')


# x = int(input("enter an  enterger: "))

# ans = 0

# while ans ** 3 < abs(x):
#     ans += 1

# if ans ** 3 != abs(x):
#     print(x, 'is not perfect value')
# else:
#     print(f'cube root of {x} is: {ans} ')


# def find_balance(string):
#     counter = 0

#     for ch in string:
#         if ch == '{':
#             counter += 1
#         elif ch == '}':
#             counter -= 1

#     return counter == 0


# print(find_balance('{/'))


# def series0(epsilon):


# Amir Ali Eslami
# https: // github.com/ChrisKolios/CPS109_Fall2022/tree/master/Review
# Amir Ali Eslami
# Function to get the value of n such that sum is within epsilon of 4.23


# def getN(epsilon):
#     n = 0
#     total = 0
#     while abs(total - 4.23) > epsilon:
#         n = n + 1
#         total = total + 1 / n  # 1 + 1/2 + 1/3 + 1/4 + 1/5
#     return n


#     # Get the value of epsilon from the user
# epsilon = float(input('Enter the value of epsilon: '))
# print(getN(epsilon))

# number 2
# def equalPairs(a, b, c, d):
#     return a + b == c + d or a + c == b + d or a + d == b + c


# if a + b == c + d:
#     return True
# if a + c == b + d:
#     return True
# if a + d == b + c:
#     return True


# print(equalPairs(1, 2, 8, 12))

# def shopSort(productDict):
#     sorted_dict = sorted(productDict.items(), key=lambda x: x[1], reverse=True)
#     print(sorted_dict)


# x = {'water': 2.99, 'gum': 1.50, 'burger': 5.99, 'crackers': 3.00}

# shopSort(x)

# nums = [5.6, 7.44, 6.75, 4.56, 2.3]
# new_values = [2.3, 9.6, 4.564, 7.56]

# This is where the magic occurs! No more for loops

# nums.append(new_values)
# print(nums)

# The list was updated with individual values
# >> > nums
# [5.6, 7.44, 6.75, 4.56, 2.3, 2.3, 9.6, 4.564, 7.56]
# print(number_4)


# from collections import Counter


# def listMerge(listOfLists):
#     output = []

#     for li in listOfLists:
#         if sum(li) % 2 == 0:
#             output.append(sum(li))
#         else:
#             output.extend(li)

#     return output


# print(listMerge([[12, 22, 44], [12, 9], [2, 4]]))
# print(listMerge([[12], [44, 11], [4, 7, 13]]))
# print(listMerge([[88, 19], [2, 4, 8, 8, 12], [8, 7, 14, 12, 12], [18, 99]]))


# def marketResearch(cards):
#     all_cards = []
#     for card in cards:
#         for item in card:
#             all_cards.append(item)
#     print(all_cards)

#     all_cards_counter = Counter(all_cards)
#     print(all_cards_counter)
#     sorted_dict = sorted(all_cards_counter.items(),
#                          key=lambda x: x[1], reverse=True)
#     return sorted_dict[0]


# x = marketResearch([['peas', 'potatoes', 'gravy', 'chicken'], ['potatoes', 'gravy', 'beans', 'steak'], ['potatoes', 'grapes'], ['grapes', 'steak', 'beans']]
#                    )
# print(x)


# 3

# 5 cents. Nickel.
# 10 cents. Dime.
# 25 cents Quarter.
# 1 dollar. Loonie.
# 2 dollars Toonie.

# def leastCoins(toonies, loonies, quarters, dimes, nickels):

#     x = toonies*2 + loonies*1 + quarters / 4 + dimes/20 + nickels/25
#     print(x)
#     toonies = x // 2
#     temp1 = x % 2 * 100
#     loonies = (x % 2) // 1

#     quarters = temp1//4
#     print(quarters % 5)
#     dimes = (x % 2 % 4 % 5)//5
#     nickels = (x % 2 % 4 % 5 % 6)//6
#     print(toonies, loonies, quarters, dimes, nickels)


# leastCoins(2, 1, 5, 0, 2)


# def anagram(a, b):
#     # string to list
#     str1 = list(a.lower())
#     str1 = [x.replace(' ', '') for x in str1]
#     str2 = list(b.lower())
#     str2 = [x.replace(' ', '') for x in str2]
#     # sort list
#     str1.sort()
#     str2.sort()
# # join list back to string
#     str1 = ''.join(str1)
#     str2 = ''.join(str2)
#     print(str1)

#     return str1 == str2


# print(anagram('Orche stra', 'Carthorse'))


# numbers = [str(x) for x in range(1, 1001)]
# output = []
# for i in range(len(numbers)):
#     num_of_7 = numbers[i].count('7')
#     num_of_0 = numbers[i].count('0')
#     if num_of_0 > num_of_7:
#         output.append(numbers[i])

# print(len(output))
# print(output)

# def test_for_anagrams(str_1, str_2):
#     counter1 = {}
#     for c in str_1.lower():
#         counter1[c] = counter1.get(c, 0) + 1
#     counter2 = {}
#     for c in str_2.lower():
#         counter2[c] = counter2.get(c, 0) + 1

# # print statements so you can see what's going on,
# # comment out/remove at will
#     print(counter1)
#     print(counter2)

#     return counter1 == counter2


# test_for_anagrams("abcdef", "fedcba")


x = 0.0


def my_func():
    z = 0
    for i in range(10):
        z = z + 0.1


my_func()
print(z)
