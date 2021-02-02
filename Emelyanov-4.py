from turtle import *
bgcolor('pink')

t = Turtle()

side = 10
storona = 0
t.up()
t.back(200)
t.down()
while storona < 12 :

    t.left(90)
    t.color('white')
    t.forward(side * 2)
    t.right(90)
    t.color('blue')
    t.forward(side * 2)
    t.right(90)
    t.color('red')
    t.forward(side * 2)
    t.left(90)
    t.color('white')
    t.forward(side)
    t.color('red')
    t.circle(side)
    t.color('blue')
    t.forward(side)
    storona = storona + 1

t.screen.exitonclick()
