import turtle
import random
t = turtle.Turtle()
window = turtle.Screen()
window.colormode(255)
t.speed('fastest')
# t._tracer(0)

def draw_dragon(length, step, angle=45):
    if step <= 0:
        t.pencolor(random.sample(range(200,255), 3))
        t.width(2)
        t.fd(length)
    else:
        t.left(angle)
        draw_dragon(length, step - 1, 45)
        t.right(angle * 2)
        draw_dragon(length, step - 1, -45)
        t.left(angle)


window.bgcolor('grey')
draw_dragon(10, 50)
window.exitonclick()