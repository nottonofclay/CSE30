''' DO NOT FORGET TO ADD COMMENTS '''

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen


def click_button(tiles, vertex):
    print(vertex.get_connections())
    # TODO:USE UPDATE
    tiles.update(vertex.get_id())
        # gui.nametowidget(str(vertex.get_id())).configure(text='hi')

def add_button(gui, tiles, font, vertex):
    text = StringVar()
    text.set(str(vertex.get_id()))
    return Button(gui, text=vertex.get_value(), name = str(vertex.get_id()), bg='white',
                    fg='black', font=font, height=2, width=5,
                    command = lambda : click_button(tiles, vertex))

if __name__ == '__main__':

    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Comic Sans MS', size='25', weight='bold')
    buttons = []
    for i in tiles.tiles:
        new_button = add_button(gui, tiles, font, i)
        buttons.append(new_button)

    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)

    # button = Button(gui, text='shuffle', name=StringVar(value='shuffle'),
    #                     bg='white', fg='black', font=font, height=2,
    #                     width=10, command = lambda : click_button('shuffle') )
    tiles.draw()
    gui.mainloop()
