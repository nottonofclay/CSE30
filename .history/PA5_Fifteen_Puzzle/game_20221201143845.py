''' DO NOT FORGET TO ADD COMMENTS '''

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen


def click_button(name):
    global buttonsClick
    gui.nametowidget(name).configure(bg='blue')

def add_button(gui, value, font, name):
    text = StringVar()
    text.set(str(value))
    return Button(gui, text=str(value), name = name, bg='white',
                    fg='black', font=font, height=2, width=5,
                    command = lambda : click_button(name))

if __name__ == '__main__':

    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Comic Sans MS', size='25', weight='bold')
    for i in tiles.tiles:
        new_button = add_button(gui, )
    b1  = add_button(gui,  1, font, 'b1')
    b2  = add_button(gui,  2, font, 'b2')
    b3  = add_button(gui,  3, font, 'b3')
    b4  = add_button(gui,  4, font, 'b4')
    b5  = add_button(gui,  5, font, 'b5')
    b6  = add_button(gui,  6, font, 'b6')
    b7  = add_button(gui,  7, font, 'b7')
    b8  = add_button(gui,  8, font, 'b8')
    b9  = add_button(gui,  9, font, 'b9')
    b10 = add_button(gui, 10, font, 'b10')
    b11 = add_button(gui, 11, font, 'b11')
    b12 = add_button(gui, 12, font, 'b12')
    b13 = add_button(gui, 13, font, 'b13')
    b14 = add_button(gui, 14, font, 'b14')
    b15 = add_button(gui, 15, font, 'b15')
    b16 = add_button(gui, '', font, 'b16')

    buttons = [ b1 , b2 , b3 , b4,
                b5 , b6 , b7 , b8,
                b9 , b10, b11, b12,
                b13, b14, b15, b16 ]

    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)

    # the key argument name is used to identify the button
    # gui.nametowidget(name1).configure(bg='white')

    # add buttons to the window
    # use .grid() or .pack() methods
    # update the window
    gui.mainloop()
