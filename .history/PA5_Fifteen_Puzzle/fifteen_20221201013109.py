''' DO NOT FORGET TO ADD COMMENTS '''

import numpy as np
from graph import Graph
from random import choice

class Fifteen:

    def __init__(self, size = 4):
        self.tiles = Graph()
        for i in range(1,size**2+1):
            self.tiles.add_vertex(i)
            for j in self.tiles:
                if (abs(i-j.id) == 1) and (j.id % size != 0):
                    self.tiles.add_edge(i, j)
                elif (abs(i-j.id) % size == 0):
                    self.tiles.add_edge(i,j)

    def update(self, move):
        pass

    def transpose(self, i, j):
        pass

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice (self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index

    def is_valid_move(self, move):
        pass

    def is_solved(self):
        pass

    def draw(self):
        pass

    def __str__(self):
        pass


if __name__ == '__main__':

    game = Fifteen()
    for i in game.tiles:
        print(i)
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_valid_move(15) == True
    # assert game.is_valid_move(12) == True
    # assert game.is_valid_move(14) == False
    # assert game.is_valid_move(1) == False
    # game.update(15)
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    # game.update(15)
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_solved() == True
    # game.shuffle()
    # assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_solved() == False


    '''You should be able to play the game if you uncomment the code below'''
    '''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    '''



