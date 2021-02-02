from turtle import *
bgcolor('pink')

t = Turtle()

side = 100
storona = 0
t.right(90)
t.forward(300)
t.left(90)
t.forward(230)
while storona < 4 :

    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(530)
    storona = storona + 1

t.screen.exitonclick()