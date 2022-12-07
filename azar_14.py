# s1 = 'a'
# s2 = 'b'
# print(ord(s1))
# print(ord(s2))
# if s1 > s2:
#     print('Ok')

x = 9
epsilon = 0.01
guess = 0
step = 0
low = 1
high = x
ans = (low + high)/2
while abs(ans**2 - x) >= epsilon:

    step += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2

print(ans, step)
