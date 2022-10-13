import turtle
t = turtle.Turtle()
t.speed('fastest')
window = turtle.Screen()
def draw_tree(branch_length, levels):
    if levels > 0:
        t.pencolor('blue')
        t.fd(branch_length)
        t.rt(20)
        # first outer branch
        print(f'section 1: levels--{levels}, length--{branch_length}')

        t.pencolor('green')
        draw_tree(branch_length * 3/4, levels - 1)
        # reorienting for next branch
        t.lt(20)
        t.bk(branch_length)
        print(f'section 2: levels--{levels}, length--{branch_length}')

        # t.pencolor('red')
        # draw_tree(branch_length * 3/4, levels - 1)
        # print(f'section 3: levels--{levels}, length--{branch_length}')
    else:
        t.dot(10, 'green')


t.lt(90)
draw_tree(80, 4)
window.exitonclick()