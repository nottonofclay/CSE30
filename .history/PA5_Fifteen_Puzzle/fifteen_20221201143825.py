''' DO NOT FORGET TO ADD COMMENTS '''

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
            if (i.value == move):
                move_tile = i.id
        if (self.is_valid_move(move_tile, other=empty_tile)):
            self.transpose(move_tile, empty_tile)

    def transpose(self, i, j):
        if (self.is_valid_move(i,j)):
            self.tiles.get_vertex(i).value, self.tiles.get_vertex(j).value = self.tiles.get_vertex(j).value, self.tiles.get_vertex(i).value

    def shuffle(self, steps=30):
        start = 16
        for i in range(steps):
            move = choice(self.tiles.get_vertex(start).get_connections())
            self.transpose(start, move)
            start = move

    def is_valid_move(self, initial, other=16):
        if (initial in self.tiles.get_vertex(other).get_connections()):
            return True
        return False

    def is_solved(self):
        solutions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ' ']
        if (self.tiles.get_verticies_values() == solutions):
            return True
        return False

    def draw(self):
        board_vals = [str(i).rjust(2) for i in self.tiles.get_verticies_values()]
        print('+----+----+----+----+')
        print('| {} | {} | {} | {} |'.format(board_vals[0], board_vals[1],  board_vals[2],  board_vals[3]))
        print('+----+----+----+----+')
        print('| {} | {} | {} | {} |'.format(board_vals[4], board_vals[5],  board_vals[6],  board_vals[7]))
        print('+----+----+----+----+')
        print('| {} | {} | {} | {} |'.format(board_vals[8], board_vals[9],  board_vals[10], board_vals[11]))
        print('+----+----+----+----+')
        print('| {} | {} | {} | {} |'.format(board_vals[12],board_vals[13], board_vals[14], board_vals[15]))
        print('+----+----+----+----+')

    def __str__(self):
        output = ' ' + str(self.tiles.get_vertex(1).value) + ' '
        for i in range(2, len(self.tiles.get_verticies_values())):
            current = self.tiles.get_vertex(i)
            previous = self.tiles.get_vertex(i-1)
            if (current.id in previous.get_connections()):
                try:
                    if (type(current.value) == str):
                        output += ' ' + str(current.value) + ' '
                        break
                    elif (current.value < 10) and (previous.value < 10):
                        output += ' ' + str(current.value) + ' '
                    else:
                        output += str(current.value) + ' '
                except:
                    output += ' ' + str(current.value) + ' '
            else:
                if (current.value == ' '):
                    output += '\n' + current.value + ''
                elif (current.value < 10):
                    output += '\n ' + str(current.value) + ' '
                else:
                    output += '\n' + str(current.value) + ' '
        if (self.tiles.get_vertex(len(self.tiles.get_verticies_values())).value == ' '):
            output += ' '
        elif (self.tiles.get_vertex(len(self.tiles.get_verticies_values())).value < 10):
            output += ' '
        output += str(self.tiles.get_vertex(len(self.tiles.get_verticies_values())).value) + ' \n'
        return output


if __name__ == '__main__':

    # game = Fifteen()
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



    game = Fifteen()
    for i in game.tiles:
        print(i)
    # game.shuffle()
    # game.draw()
    # while True:
    #     move = input('Enter your move or q to quit: ')
    #     if move == 'q':
    #         break
    #     elif not move.isdigit():
    #         continue
    #     elif (int(move) not in game.tiles.get_verticies_values()):
    #         continue
    #     game.update(int(move))
    #     game.draw()
    #     if game.is_solved():
    #         break
    # print('Game over!')
