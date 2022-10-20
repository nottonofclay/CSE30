class Board:
      def __init__(self):
            # board is a list of cells that are represented
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
      def get_size(self):
            return self.size ** 2
      def get_winner(self):
            return self.winner
      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            index = valid_choices.index(cell)
            self.board[index] = sign

      def isempty(self, cell):
            cell_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            # return True if the cell is empty (not marked with X or O)
            if (self.board[cell_choices.index(cell)] == ' '):
                  return True
            else:
                  return False
      def isdone(self):
            done = False
            # top horizontal, left vertical, left to right diagonal
            if (self.board[0] != ' ') and (self.board[0] == self.board[3] == self.board[6]):          # top horizontal
                        self.winner = self.board[0]
                        return True
            elif (self.board[0] != ' ') and (self.board[0] == self.board[1] == self.board[2]):        # left vertical
                        self.winner = self.board[0]
                        return True
            elif (self.board[0] != ' ') and (self.board[0] == self.board[4] == self.board[8]):        # left/right diag
                        self.winner = self.board[0]
                        return True
            elif (self.board[6] != ' ') and (self.board[6] == self.board[7] == self.board[8]):        # right vertical
                  self.winner = self.board[6]
                  return True
            elif (self.board[6] != ' ') and (self.board[6] == self.board[4] == self.board[2]):        # right/left diag
                  self.winner = self.board[6]
                  return True
            elif (self.board[1] != ' ') and (self.board[1] == self.board[4] == self.board[7]):        # middle horizontal
                  if(self.board[1] == self.board[4] == self.board[7]):
                        self.winner = self.board[1]
                        return True
            elif (self.board[2] != ' ') and (self.board[2] == self.board[5] == self.board[8]):        # bottom horizontal
                  self.winner = self.board[2]
                  return True
            elif (self.board[3] != ' ') and (self.board[3] == self.board[4] == self.board[5]):        # middle vertical
                  self.winner = self.board[3]
                  return True
            elif (' ' not in self.board):
                  self.winner = ''
                  return True
            return done
      def show(self):
            # draw the board
            # need to complete the code
            print('   A   B   C')
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[3], self.board[6]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[1], self.board[4], self.board[7]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[2], self.board[5], self.board[8]))
            print(' +---+---+---+')