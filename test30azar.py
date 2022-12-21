# from sample.azar_17 import my_func
# my_func(1)

import turtle

s = turtle.Screen()
s.bgcolor('orange')
# s.bgpic('mario.png')
p = turtle.Pen()
p.pensize(4)
COLORs = ['red', 'green', 'blue', 'black']
for i in range(12):
    p.pencolor(COLORs[i % 4])
    for i in range(4):
        p.fd(100)
        p.left(90)
    p.left(30)

s.exitonclick()
