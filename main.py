import turtle
from turtle import *

wn = Screen()
wn.bgcolor('black')
t = turtle.Turtle()
t.pencolor('white')

def curve():
    for i in range(50):
        t.rt(4)
        t.fd(4)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(117)
    curve()
    t.lt(120)
    curve()
    t.fd(108)
    t.end_fill()

heart()
t.ht()

def write(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.color('w
    style = ("Stencil Std", 20, "italic")
    t.write(message, font=style)


write('хомячок', (-50, 87))

wn.mainloop()