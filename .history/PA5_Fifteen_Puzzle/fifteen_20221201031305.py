''' DO NOT FORGET TO ADD COMMENTS '''

import numpy as np
from graph import Graph
from random import choice

class Fifteen:

    def __init__(self, size = 4):
        self.tiles = Graph()
        for i in range(1,size**2+1):
            if (i == 16):
                self.tiles.add_vertex(i,value=' ')
            else:
                self.tiles.add_vertex(i,value=i)
            for j in self.tiles:
                if (i == j.id):
                    continue
                elif (abs(i-j.id) == 1) and (j.id % size != 0):
                    self.tiles.add_edge(i, j.id)
                elif (abs(i-j.id) / size == 1):
                    self.tiles.add_edge(i, j.id)

    def update(self, move):
        for i in self.tiles:
            if (i.value == ' '):
                empty_tile = i.id
        if (self.is_valid_move(move, empty_tile)):
            self.transpose(move, empty_tile)

    def transpose(self, i, j):
        if (self.is_valid_move(i,j)):
            self.tiles.get_vertex(i).value, self.tiles.get_vertex(j).value = self.tiles.get_vertex(j).value, self.tiles.get_vertex(i).value

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice (self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index

    def is_valid_move(self, initial, other):
        if (initial in self.tiles.get_vertex(other).get_connections()):
            return True
        return False

    def is_solved(self):
        solutions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ' ']
        if (self.tiles.get_verticies_values() == solutions):
            return True
        return False

    def draw(self):
        pass

    def __str__(self):
        output = str(self.tiles.get_vertex(1).value)
        for i in range(2, len(self.tiles.get_verticies_values())+1):
            if (self.tiles.get_vertex(i).value in self.tiles.get_vertex(i-1).get_connections()):
                print(str(self.tiles.get_vertex(i).value))
                output += str(self.tiles.get_vertex(i).value) + ' '
            else:
                output += '\n' + str(self.tiles.get_vertex(i).value) + ' '
        return output


if __name__ == '__main__':

    game = Fifteen()
    print(str(game))
    game.update(15)
    print(str(game))
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



