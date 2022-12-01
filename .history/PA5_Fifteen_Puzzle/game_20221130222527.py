''' DO NOT FORGET TO ADD COMMENTS '''

from tkinter import *
import tkinter.font as font
#from fifteen import Fifteen


def clickButton():
    pass

def addButton(gui, value, font):
    text = StringVar()
    text.set(str(value))
    name = value
    return Button(gui, text=str(value), name = str(value), bg='white',
                    fg='black', font=font, height=2, width=5,
                    command = lambda : clickButton())

if __name__ == '__main__':

    # make tiles
    #tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')
    b1  = addButton(gui,  1, font)
    b2  = addButton(gui,  2, font)
    b3  = addButton(gui,  3, font)
    b4  = addButton(gui,  4, font)
    b5  = addButton(gui,  5, font)
    b6  = addButton(gui,  6, font)
    b7  = addButton(gui,  7, font)
    b8  = addButton(gui,  8, font)
    b9  = addButton(gui,  9, font)
    b10 = addButton(gui, 10, font)
    b11 = addButton(gui, 11, font)
    b12 = addButton(gui, 12, font)
    b13 = addButton(gui, 13, font)
    b14 = addButton(gui, 14, font)
    b15 = addButton(gui, 15, font)
    b16 = addButton(gui, '', font)

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
