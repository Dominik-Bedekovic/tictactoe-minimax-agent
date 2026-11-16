from .board import TicTacToeBoard
import time
import random

class TicTacToeMinimaxAgent():
    def __init__(self, board: TicTacToeBoard, random_chance=0, is_benchmark=False, is_prune=True):
        self.board = board
        self.nodes_expanded = 0 
        self.random_chance = random_chance
        self.is_prune = is_prune
        self.is_benchmark = is_benchmark
        if self.is_benchmark:
            self.num_of_searches = 0
            self.elapsed_time = 0

    def minimax(self, is_maximising:bool, alpha=-float('inf'), beta=float('inf')):
        self.nodes_expanded += 1
        if self.is_benchmark:
            self.num_of_searches += 1
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
                if self.is_prune:
                    score= self.minimax(False, alpha, beta)
                else:
                    score = self.minimax(False)
                bestScore = max(score, bestScore)
                if self.is_prune:
                    alpha = max(alpha, bestScore)
            else:
                self.board[i][j] = 'O'
                if self.is_prune == True:
                    score = self.minimax(True, alpha, beta)
                else:
                    score = self.minimax(True)
                bestScore = min(score, bestScore)
                if self.is_prune:
                    beta = min(beta, bestScore)

            self.board[i][j] = ' '

            if self.is_prune == True:
                if beta <= alpha:
                    break

        return bestScore

    def get_next_move(self):
        self.nodes_expanded = 0
        if self.board.check_winner() is not None:
            return None
        if self.board.current_player != 'O':
            raise ValueError("This agent plays O; call it on O's turn.")

        if self.is_benchmark:
            start = time.process_time()

        moves = self.board.get_possible_moves()

        if (random.random() <= self.random_chance):

            random_move = random.choice(moves)

            return random_move

        bestScore = float('inf')
        bestMove = None

        for move in moves:
            i, j = move
            self.board[i][j] = 'O'
            score= self.minimax(True)

            if score < bestScore:
                bestScore = score
                bestMove = move

            self.board[i][j] = ' '

        if self.is_benchmark:
            end = time.process_time()
            self.elapsed_time = (end - start) * 1000

        return bestMove
