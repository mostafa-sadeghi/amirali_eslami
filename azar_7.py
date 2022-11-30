
# try:
#     x = int(input("first number >"))
#     y = int(input("second number >"))
#     z = x/y
# except ValueError:
#     print('values are invalid')
# except ZeroDivisionError:
#     print('second number is zero ')
# except:
#     print('other exception')
# else:
#     print('no exception occured')
# finally:
#     print('finally')
# print('outside')


# try:
#     f = open('stth.txt', 'r')
# except:
#     print('exception')

# finally:
#     if FileExistsError:
#         print('ballala')

#     else:
#         f.close()


# while True:
#     try:
#         x = int(input('> '))
#         break
#     except:
#         print('Input not an int')
# print('correct input')


fn = input('enter file name: ')
data = []
try:
    file = open(fn, 'r')
    try:
        for row in file:
            if row != '\n':
                temp = row[:-1].split(',')
                data.append(temp)
    finally:
        file.close()

except IOError:
    print(f'can not open {fn}')

gradesData = []
if data:
    for student in data:
        try:
            gradesData.append([student[0:2], [student[2]]])
        except:
            gradesData.append([student[0:2], []])
            print("exception")


print(data)
print(gradesData)
