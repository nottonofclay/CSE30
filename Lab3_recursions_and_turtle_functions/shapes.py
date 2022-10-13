import turtle

t = turtle.Turtle()                             # creating turtle object
window = turtle.Screen()
angle = 0                                       # var for recusive var

def polygon(size, n):                           # draws polygon using loops
    t.pendown()
    t.begin_fill()
    for i in range(n):
        t.fd(size)
        t.rt(360 / n)
    t.end_fill()

def polygon_recursive(size,n):                  # draws polygon using recursion
    global angle
    if angle == 0:                              # saves angle in galobal var
        angle = 360 / n
    t.pendown()
    t.begin_fill()
    if n <= 0:                                  # exiting recursion
        angle = 0
        return n
    else:                                       # loops thru here
        t.fd(size)
        t.rt(angle)
        return polygon_recursive(size, n-1)

def star(size,n, density = 2):
    t.pendown()
    t.begin_fill()
    if (n % 2 != 0):                            # if odd uses formula
        for i in range(n):
            t.fd(size)
            t.rt(360 * (density / n))
    else:                                       # if even does smth else cuz im lwk dumb
        for i in range(n):
            t.fd(size/(n/2))
            for j in range(3):
                t.lt(120)
                t.fd(size/(n/2))
            t.rt(360 / n)

def star_recursive(size,n, density = 2):
    global angle
    t.pendown()
    t.begin_fill()
    if angle == 0:                              # okay it says angle but it's actually sides here srry
        angle = n
    if n == 0:
        angle = 0
        return n
    else:
        if (angle % 2 != 0):
            t.fd(size)
            t.rt(360 * (density / angle))
            star_recursive(size, n-1)
        else:
            t.fd(size/(angle/2))
            for i in range(3):
                t.lt(120)
                t.fd(size/(angle/2))
            t.rt(360 / angle)
            star_recursive(size, n-1)

polygon_recursive(200,5)
star_recursive(200, 5)
star(200, 8)
window.exitonclick()

