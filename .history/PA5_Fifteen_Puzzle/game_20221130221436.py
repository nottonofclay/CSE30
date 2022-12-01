''' DO NOT FORGET TO ADD COMMENTS '''

from tkinter import *
import tkinter.font as font
#from fifteen import Fifteen


def clickButton():
    pass

def addButton(gui, value):
    font = font.Font(family='Helveca', size='25', weight='bold')
    text = StringVar()
    text.set(str(value))
    name = value
    return(Button(gui, text=text, name = text, bg='white',
                    fg='black', font=font, height=2, width=5,
                    command = lambda : clickButton()))

if __name__ == '__main__':
    font = font.Font(family='Helveca', size='25', weight='bold')
    # make tiles
    #tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    b1 = addButton(gui, 1)
    b2 = addButton(gui, 2)

    buttons = [b1, b2]

    for i in buttons:
        i.pack()

    # the key argument name is used to identify the button
    # gui.nametowidget(name1).configure(bg='white')

    # add buttons to the window
    # use .grid() or .pack() methods
    # update the window
    gui.mainloop()
