from asyncio import SelectorEventLoop
from pyclbr import Class
from random import choice

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            return self.sign
      def get_name(self):
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            while True:
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
                  if cell in valid_choices:
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                        else:
                              print('You did not choose correctly.')
                  else:
                        print('You did not choose correctly.')

class AI(Player):
      def __init__(self, name, sign, board):
            super().__init__(name, sign)

      def choose(self, board):
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            while True:
                  if board.isempty(choice(valid_choices)):
                        board.set(choice(valid_choices), self.sign)
                        break

class MiniMax(Player):
      def __init__(self, name, sign, board):
            super().__init__(name, sign)
      def choose(self, board):
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)
      def determine_sign(self, player):
            if player:
                  return self.sign
            else:
                  if self.sign == 'X':
                        return 'O'
                  else:
                        return 'X'
      def minimax(self, board, self_player, start):
            # check the base conditions
            score = 0
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            if board.isdone():
                  # self is a winner
                  if board.get_winner() == 'X':
                        return 1
                  # self is a looser (opponent is a winner)
                  elif board.get_winner() == 'O':
                        return -1
                  # is a tie
                  else:
                        return 0
            else:
                  min = float('inf')
                  max = float('-inf')
                  for i in range(board.get_size()):
                        if (board.isempty(valid_choices[i])):
                              board.set(valid_choices[i], self.determine_sign(self_player))
                              score = MiniMax.minimax(self, board, not self_player, False)
                              board.show()
                              print(f'score: {score}')
                              # if (self_player) and score > max:
                              #       max = score
                              # elif (not self_player) and score < min:
                              #       min = score
                              board.set(valid_choices[i], ' ')








                  # make a move (choose a cell) recursively
                  # use the pseudocode given to you above to implement the missing code


# class SmartAI(Player):
#       def __init__(self, name, sign, board):
#             super().__init__(name, sign)
#       def choose(self, board):
#             if board.isempty('B2'):
#                   board.set('B2', self.sign)
#             elif board.isempty('A1')
