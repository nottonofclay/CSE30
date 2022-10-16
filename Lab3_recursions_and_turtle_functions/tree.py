import turtle
import random
t = turtle.Turtle()
t._tracer(100)
window = turtle.Screen()
window.colormode(255)

def draw_tree(branch_length, levels, angle):
    if levels < 0:                                          # drawing random color for leaves
        t.pencolor([random.randint(190, 255),
            random.randint(80, 200), 9])
        for i in range(4):
            t.rt(90)
            t.fd(branch_length * 1.3)
            t.dot(branch_length * 1.3)

        t.pencolor((92, 64, 51))                            # change colour back to brown
        return levels
    else:
        t.pencolor((92, 64, 51))                            # change colour to brown
        t.width(levels * 2)

        t.fd(branch_length)                                 # drawing left branch
        t.lt(angle)
        draw_tree(branch_length * 3/4, levels - 1, angle)

        t.width(levels * 2)                                 # draws right branch
        t.rt(angle * 2)
        draw_tree(branch_length * 3/4, levels - 1, angle)

        t.lt(angle)                                         # orienting and then going backwards
        t.penup()
        t.bk(branch_length)
        t.pendown()



t.lt(90)                                                    # moves so pointing up and lower on screen
t.penup()
t.bk(200)
t.pendown()
draw_tree(100, 10, 20)
window.exitonclick()