# turtle race
from turtle import *
from random import randint
import time

def set_turtles(colors):
    turtles = []
    for color in colors:
        t = Turtle()
        t.color(color)
        t.shape("turtle")
        t.speed('fastest')
        turtles.append(t)
    return turtles

def draw_track(start, finish):
    t = Turtle()
    t.speed('fastest')
    t.penup()
    t.goto(-200, -150)
    t.pendown()
    t.write("Time Elapsed: ")
    position, size, step = 100, 200, 40
    count = 0
    for line in range(start, finish + step, step):
        t.penup()
        t.goto(line,position+10)
        if line == start:
            t.color("blue")
            t.pensize(10)
            t.write("START")
        elif line == finish:
            t.color("red")
            t.pensize(10)
            t.write("FINISH")
        else:
            t.color("grey")
            t.pensize(1)
            t.write(count)
        t.goto(line,position)
        count += 1
        t.right(90)
        t.pendown()
        t.forward(size)
        t.left(90)

def isfinish(t, finish):
    x, y = t.pos()
    if x < finish:
        return False
    else:
        return True

def finished_sequence(t):
    winner = Turtle()
    winner.hideturtle()
    winner.penup()
    winner.goto(t.pos())
    winner.pendown()
    winner.write('WINNER!')

    restart = Turtle()
    restart.penup()
    restart.goto(100, -120)
    restart.write('RESTART', align='center')
    restart.goto(100, -150)
    restart.shape('circle')
    restart.shapesize(2.5, 2.5, 2)
    restart.fillcolor('green')

    exit = Turtle()
    exit.penup()
    exit.goto(180, -120)
    exit.write('EXIT', align='center')
    exit.goto(180, -150)
    exit.shape('circle')
    exit.shapesize(2.5, 2.5, 2)
    exit.fillcolor('red')
    exit.write('EXIT', align='center')
    while True:
        restart.onclick(new_race)
        exit.onclick(end_screen)

def new_race(x, y):
    s.clear()
    start = -200
    finish = 200

    draw_track(start, finish)
    turtles = set_turtles(["yellow", "crimson", "aqua", "green", "purple"])
    race(turtles, start, finish)



def end_screen(x, y):
    s.clear()
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-180, 0)
    t.write('Thanks for Playing!', font=('', 30,''))
    time.sleep(3)
    bye()



def race(turtles, start, finish):
    # y position
    position = 80
    distance = 40
    timer = Turtle()
    timer.penup()
    timer.hideturtle()
    timer.goto(-120, -150)
    start_time = time.time()
    last_time = start_time
    for t in turtles:
        t.penup()
        t.left(180)
        t.goto(start, position)
        position -= distance
        t.left(180)
        t.pendown()
    done = False
    while not done:
        timer.pendown()
        for t in turtles:
            timer.write(f'{round((time.time() - last_time), 2)}')
            t.forward(randint(1,10))
            if isfinish(t, finish):
                timer.write(f'{round((time.time() - last_time), 3)}')
                done = True
                finished_sequence(t)
            else:
                timer.clear()

# main program
s = Screen()     # make a canvas window
s.setup(500, 400)
s.bgcolor("white")
s.title("Turtle Race")
start = -200
finish = 200

draw_track(start, finish)
turtles = set_turtles(["yellow", "crimson", "aqua", "green", "purple"])
race(turtles, start, finish)

