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
    return(Button(gui, text=value, name = str(text), bg='white',
                    fg='black', font=font, height=2, width=5,
                    command = lambda : clickButton()))

if __name__ == '__main__':

    # make tiles
    #tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    text1 = StringVar()
    text1.set('1')
    name1 = 1
    button1 = Button(gui, textvariable=text1, name=str(name1),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())

    # the key argument name is used to identify the button
    # gui.nametowidget(name1).configure(bg='white')

    # add buttons to the window
    # use .grid() or .pack() methods
    button1.pack()
    # update the window
    gui.mainloop()
