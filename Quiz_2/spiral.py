import turtle
import math

window = turtle.Screen()
# draw a spiral
def draw_spiral(t, segments, size, angle):
    t.pendown()
    if (size == segments):
        return segments
    else:
        t.fd(size)
        t.lt(angle)
        return draw_spiral(t, segments, size + 1, angle)

# driver code
if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(400, 400)
    t = turtle.Turtle()
    t.pen(pencolor='dark violet', pensize=2, speed=0)
    t.penup()
    t.home()
    draw_spiral(t, 80, 2, 92)
    window.exitonclick()