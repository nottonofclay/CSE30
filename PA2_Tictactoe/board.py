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
             # optional, return the board size (an instance size)
      def get_winner(self):
            # return the winner's sign O or X (an instance winner)     
      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            valid_choices = ['A1', 'A2', ...]
            index = valid_choices.index(cell)
            self.board[index] = sign
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            
      def isdone(self):
            done = False
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            
            return done
      def show(self):
            # draw the board
            # need to complete the code
            print('   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[1], ?)
            print(' +---+---+---+')
2|   |   |   |
 +---+---+---+
3|   |   |   |
 +---+---+---+

               
