from tictactoe.board import TicTacToeBoard
from tictactoe.agent import TicTacToeMinimaxAgent

board = TicTacToeBoard()
board.make_move(0, 0)
board.make_move(1, 1)
board.make_move(0, 1)
agent = TicTacToeMinimaxAgent(board, 1)
print(agent.get_next_move())