from tictactoe.board import TicTacToeBoard
from tictactoe.agent import TicTacToeMinimaxAgent


def test_new_board_has_nine_possible_moves():
    board = TicTacToeBoard()
    moves = board.get_possible_moves()
    assert len(moves) == 9


def test_one_move_leaves_eight_possible_moves():
    board = TicTacToeBoard()
    board.make_move(0, 0)
    moves = board.get_possible_moves()
    assert len(moves) == 8


def test_x_wins_by_being_three_in_a_row():
    board = TicTacToeBoard()
    board.make_move(0, 0)
    board.make_move(1, 0)
    board.make_move(0, 1)
    board.make_move(1, 1)
    board.make_move(0, 2)
    assert board.check_winner() == 'X'

def test_winning_line_horizontal():
    board = TicTacToeBoard()
    board.make_move(0, 0)
    board.make_move(1, 0)
    board.make_move(0, 1)
    board.make_move(1, 1)
    board.make_move(0, 2)
    assert board.get_winning_line() == ((0, 0), (0, 1), (0, 2))    

def test_winning_line_vertical():
    board = TicTacToeBoard()
    board.make_move(0, 0)
    board.make_move(0, 2)
    board.make_move(1, 0)
    board.make_move(1, 2)
    board.make_move(2, 0)
    assert board.get_winning_line() == ((0, 0), (1, 0), (2, 0))    

def test_winning_line_diagonal_left():
    board = TicTacToeBoard()
    board.make_move(0, 0)
    board.make_move(0, 2)
    board.make_move(1, 1)
    board.make_move(1, 2)
    board.make_move(2, 2)
    assert board.get_winning_line() == ((0, 0), (1, 1), (2, 2))    

def test_winning_line_diagonal_right():
    board = TicTacToeBoard()
    board.make_move(0, 2)
    board.make_move(0, 0)
    board.make_move(1, 1)
    board.make_move(1, 2)
    board.make_move(2, 0)
    assert board.get_winning_line() == ((0, 2), (1, 1), (2, 0))    

def test_minimax_agent():
    board = TicTacToeBoard()
    board.make_move(0, 0)
    board.make_move(1, 1)
    board.make_move(0, 1)
    agent = TicTacToeMinimaxAgent(board, 0)
    assert agent.get_next_move() == (0, 2) 

def test_random_agent():
    board = TicTacToeBoard()
    board.make_move(0, 0)
    board.make_move(1, 1)
    board.make_move(0, 1)
    agent = TicTacToeMinimaxAgent(board, 1)
    moves = set()
    for _ in range(50):
        moves.add(agent.get_next_move())
    assert len(moves) > 1