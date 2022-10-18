class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
      def get_name(self):
            # return an instance name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'A2', ...]
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
                  if cell in ? :
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              ?
                        else:
                              ?
                  else:
                        ?
                        
                  
