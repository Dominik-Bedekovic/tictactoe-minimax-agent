from typing import Tuple, List, Optional

class TicTacToeBoard:
    def __init__(self) -> None:
        """
        Initialize the board which is a 2D board with 9 cells 3x3.

        Initiate the player and add a variable for deciding the state of the game.
        """
        self.board = [
            [' ', ' ', ' ',],
            [' ', ' ', ' ',],
            [' ', ' ', ' ',],
        ]

        self.current_player = 'X'
        self.game_over = False

    def get_possible_moves(self) -> List[Tuple[int, int]]:
        """
        Returns a list of (i,j) pairs. 
        
        Each item is a pair of indices which indicate that the move (i,j) is a legal move.

        Example return value:
        [ (0, 1), (1, 1), (2, 2) ]
        In this example return value, there are three possible cells where a 'O' or an 'X' can be drawn.
        """     
        board = self.board
        moves = []
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == ' ':
                    moves.append( (i,j) )
        return moves
    
    def make_move(self, row:int, col:int) -> Optional[str]:
        """This will update the board.
        At position (row,col) the symbol corresponding to the current player (self.current_player)
        will be drawn.
        After the move is complete, if the game is not over, the current player will be switched to the next player.
        I.e., if this move was performed while current_player was 'X', then after completing this move,
        the current_player will automatically be updated to 'O'.
        
        Args:
            - row:int, index of the row where the board is updated
            - col:int, index of the column where the board is updated 
        """
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError('Row and column must be between 0 and 2.')
        if self.game_over or self.board[row][col] != ' ':
            return None # Ignore click if game is over or cell is occupied

        # Update the board and button
        self.board[row][col] = self.current_player

        # Check for winner or draw
        winner = self.check_winner()
        if winner in ['X', 'O', 'Draw']:
            self.game_over = True
        else:
            # winner == None, so there is no winner (the game is not done yet)
            self.__switch_player()
        return winner

    def get_game_progress(self) -> str:
        """
        Return a status message: whose turn it is, or who won.
        """
        if self.game_over is True:
            # if the game is over, check the winner
            winner = self.check_winner()
            retval = f'The game is finished. '
            retval += f"{winner} won!" if winner != 'Draw' else "It's a Draw!"
            return retval
        # the game is ongoing
        return f"It is currently {self.current_player}'s turn. "

    def __str__(self) -> str:
        row = [ '|'.join(row) for row in self.board ]
        retval = '\n-----\n'.join(row)
        return retval

    def __switch_player(self) -> None:
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self) -> Optional[str]:
        """
        Utility function which, for the current board, determines the game's result,
        and returns the winner (if there is one).
        Possible return values:
            - None, if the game is ongoing
            - 'X' if X is the winner
            - 'O' if O is the winner
            - 'Draw' if the game is finished, but there are no winners.
        """
        board = self.board

        for row in board:
            # check if there are three in a row
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]
    
        for col in range(3):
            # check if the winner has three in a column
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                return board[0][col]
        
        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return board[0][2]
    
        # if none of the winning lines are met,
        # check if there are empty spaces left (the game isn't finished while empty spaces remain)
        for row in board:
            if ' ' in row:
                return None
    
        # no winner
        return 'Draw'

    def get_winning_line(self) -> Tuple[Tuple[int, int], ...]:
        """
        Return the three winning cells as (row, col) pairs,
        or an empty tuple if nobody has won.

        Checked in order: rows, columns, top-left to bottom-right diagonal,
        top-right to bottom-left diagonal.
        """    
        winner = self.check_winner()

        winner_list = list()
        if winner == 'X' or winner == 'O':
            for i in range(3):
                if self.board[i][0] == winner:
                    if self.board[i][1] == winner and self.board[i][2] == winner:
                        winner_list = [(i, 0), (i, 1), (i, 2)]
                        break
                if self.board[0][i] == winner:
                    if self.board[1][i] == winner and self.board[2][i] == winner:
                        winner_list = [(0, i), (1, i), (2, i)]
                        break

        if (self.board[0][0] == winner and self.board[1][1] == winner and self.board[2][2] == winner):
            winner_list = [(0, 0), (1, 1), (2, 2)]

        if (self.board[0][2] == winner and self.board[1][1] == winner and self.board[2][0] == winner):
            winner_list = [(0, 2), (1, 1), (2, 0)]
                            

        return tuple(winner_list)

    def __getitem__(self, index):
        return self.board[index]
