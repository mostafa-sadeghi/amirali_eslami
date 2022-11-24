# input > word_digits = "1000100011002200"
# output > ['1', '000', '1', '000', '11', '00', '22', '00']

# word_digits = "0001100110"
# count = 0
# start = 0
# output = []
# for i in range(len(word_digits)-1):
#     if word_digits[i] == word_digits[i+1]:  # count: 6      i:5     start: 4
#         count += 1
#     else:
#         output.append(word_digits[start:count+1])
#         start = count + 1
#         count += 1
# else:
#     output.append(word_digits[start:count + 1])


# print(output)


# for i in range(1, 5):

#     print(i)
#     if i == 3:
#         break

# else:
#     print("end")


###########################################################

import random
import datetime


def getBirthdays(numberofBirthdays):
    """Return numbers of random birthdays,
    Parameter: int
    Returns:list

    """
    birthdays = []
    for _ in range(numberofBirthdays):
        epoch_time = datetime.date(2022, 1, 1)
        # random.seed(30)
        number_of_days = datetime.timedelta(random.randrange(0, 365))
        birthday = epoch_time + number_of_days
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """
    birthdays: list
    Returns: None if there is'nt any matches else date object
    """
    if len(birthdays) == len(set(birthdays)):
        return None

    for i, x in enumerate(birthdays):
        for j, y in enumerate(birthdays[i+1:]):
            if x == y:
                return x


MONTHS = ('Jan', 'Feb', 'Mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec')


while True:
    print('how many birthdays do you want? max : 70')
    response = input("> ")
    # input validation
    if response.isdecimal() and (0 < int(response) <= 70):
        numBDays = int(response)
        break


birthdays = getBirthdays(numBDays)

for birthday in birthdays:
    month_name = MONTHS[birthday.month-1]
    day = f'{month_name} {birthday.day}'
    print(day)


match = getMatch(birthdays)

print()
print()
print()
print()
print('###################################')


if match == None:
    print("there is no matching birthday!")
else:
    month_name = MONTHS[match.month-1]
    day = f'{month_name} {match.day}'
    print(day)


print()
print()
print()
print('Our final simulation!!!')
# result saves number of matches
result = 0


for i in range(10_000):
    if i % 1000 == 0:
        print('.........')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        result += 1


prob = result / 10_000 * 100

print("result is : ", result)
