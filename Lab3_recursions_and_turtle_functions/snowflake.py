import turtle

window = turtle.Screen()
t = turtle.Turtle()
t.speed('fastest')

def draw_snowflake(length, step):
    # base call
    if step == 0:
        t.fd(length)
        return step
    else:
        draw_snowflake(length/3, step - 1)
        t.rt(60)
        draw_snowflake(length/3, step - 1)
        t.lt(120)
        draw_snowflake(length/3, step - 1)
        t.rt(60)
        draw_snowflake(length/3, step - 1)


t.penup()
t.bk(200)
t.pendown()
for i in range(3):
    draw_snowflake(200,4)
    t.lt(120)

t = turtle.Turtle()
window.exitonclick()