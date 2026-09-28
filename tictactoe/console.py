"""Terminal fallback requiring only the Python standard library."""
from .board import TicTacToeBoard
from .agent import TicTacToeMinimaxAgent


def play():
    board = TicTacToeBoard()
    agent = TicTacToeMinimaxAgent(board)
    print('You are X. Enter row and column from 1 to 3, e.g. 2 2. Enter q to quit.')
    while not board.game_over:
        print('\n' + str(board))
        if board.current_player == 'X':
            try:
                value = input('Your move: ').strip()
            except (EOFError, KeyboardInterrupt):
                print('\nGoodbye!')
                return
            if value.lower() == 'q':
                return
            try:
                row, col = (int(part) - 1 for part in value.split())
                if (row, col) not in board.get_possible_moves():
                    raise ValueError
            except ValueError:
                print('Choose an empty cell using two numbers from 1 to 3.')
                continue
            board.make_move(row, col)
        else:
            move = agent.get_next_move()
            if move is None:
                raise RuntimeError('No move returned for an unfinished game.')
            board.make_move(*move)
            print(f'Minimax plays {move[0] + 1} {move[1] + 1} ({agent.nodes_expanded:,} nodes).')
    print('\n' + str(board))
    print(board.get_game_progress())
