class TicTacToeBoard:
    def __init__(self):
        self.board = [
            [' ', ' ', ' ',],
            [' ', ' ', ' ',],
            [' ', ' ', ' ',],
        ]

        self.current_player = 'X'
        self.game_over = False

    def get_possible_moves(self):
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
    
    def make_move(self, row:int, col:int):
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
            return  # Ignore click if game is over or cell is occupied

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

    def get_game_progress(self):
        if self.game_over is True:
            # if the game is over, check the winner
            winner = self.check_winner()
            retval = f'The game is finished. '
            retval += f"{winner} won! 🎉" if winner != 'Draw' else "It's a Draw! 😐"
            return retval
        # the game is ongoing
        return f"It is currently {self.current_player}'s turn. "

    def __str__(self):
        retval = [ '|'.join(row) for row in self.board ]
        retval = '\n-----\n'.join(retval)
        return retval

    def __switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
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

    def __getitem__(self, index):
        return self.board[index]
