from .board import TicTacToeBoard


class TicTacToeMinimaxAgent():
    def __init__(self, board: TicTacToeBoard):
        self.board = board
        self.nodes_expanded = 0

    def minimax(self, is_maximising:bool):
        self.nodes_expanded += 1
        winner = self.board.check_winner()

        if winner:
            if winner == 'Draw':
                return 0
            elif winner == 'X':
                return 1
            else:
                return -1

        bestScore = None
        if is_maximising is True:
            bestScore = -1
        else:
            bestScore = 1

        moves = self.board.get_possible_moves()

        for move in moves:
            i, j = move

            if is_maximising:
                self.board[i][j] = 'X'
                score = self.minimax(False)
                bestScore = max(score, bestScore)
            else:
                self.board[i][j] = 'O'
                score = self.minimax(True)
                bestScore = min(score, bestScore)

            self.board[i][j] = ' '

        return bestScore

    def get_next_move(self):
        self.nodes_expanded = 0
        if self.board.check_winner() is not None:
            return None
        if self.board.current_player != 'O':
            raise ValueError("This agent plays O; call it on O's turn.")

        moves = self.board.get_possible_moves()

        bestScore = float('inf')
        bestMove = None

        for move in moves:
            i, j = move
            self.board[i][j] = 'O'
            score = self.minimax(True)

            if score < bestScore:
                bestScore = score
                bestMove = move

            self.board[i][j] = ' '

        return bestMove
