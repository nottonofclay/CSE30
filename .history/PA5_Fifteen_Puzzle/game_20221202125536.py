''' DO NOT FORGET TO ADD COMMENTS '''

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
from random import choice
from time import sleep


def click_button(gui, tiles, vertex):
    if (vertex.get_value() == ' '):
        return ' '
    print(vertex.get_value())
    # TODO:USE UPDATE
    tiles.update(int(vertex.get_value()))
    tiles.draw()
    update_board(gui, tiles)

def update_board(gui, tiles):
    for i in tiles.tiles.get_vertices():
        gui.nametowidget(str(i)).configure(text=str(tiles.tiles.get_verticies_values()[i-1]))

def add_button(gui, tiles, font, vertex):
    text = StringVar()
    text.set(str(vertex.get_id()))
    return Button(gui, text=vertex.get_value(), name = str(vertex.get_id()), bg='white',
                    fg='black', font=font, height=2, width=5,
                    command = lambda : click_button(gui, tiles, vertex))

def shuffle(gui, tiles, steps=1):
    start = 16
    for i in range(steps):
        move = choice(tiles.tiles.get_vertex(start).get_connections())
        tiles.transpose(start, move)
        start = move
        update_board(gui,tiles)

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

    shuffle_button = Button(gui, text='shuffle', name='shuffle',
                        bg='white', fg='black', font=font, height=1,
                        width=10, command = lambda : shuffle(gui, tiles) )
    shuffle_button.grid(row=6, column=1, columnspan=2)


    tiles.shuffle()
    update_board(gui, tiles)

    gui.mainloop()
