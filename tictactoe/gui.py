"""Tkinter interface; game rules and search live in separate modules."""
import tkinter as tk
from .board import TicTacToeBoard
from .agent import TicTacToeMinimaxAgent


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.pending_move = None
        self.thinking = False
        root.title('Tic-Tac-Toe | Minimax')
        root.resizable(False, False)
        root.configure(bg='#172033')
        tk.Label(root, text='TIC-TAC-TOE', font=('Arial', 22, 'bold'),
                 bg='#172033', fg='white').pack(padx=30, pady=(24, 6))
        tk.Label(root, text='You are X  •  Minimax is O', font=('Arial', 11),
                 bg='#172033', fg='#b9c5d8').pack()
        self.status = tk.StringVar()
        tk.Label(root, textvariable=self.status, font=('Arial', 12),
                 bg='#172033', fg='white').pack(pady=14)
        grid = tk.Frame(root, bg='#172033')
        grid.pack(padx=24)
        self.buttons = []
        for row in range(3):
            cells = []
            for col in range(3):
                button = tk.Button(grid, text=' ', width=4, height=2,
                                   font=('Arial', 26, 'bold'), bg='#e6edf7',
                                   command=lambda r=row, c=col: self.human_move(r, c))
                button.grid(row=row, column=col, padx=4, pady=4)
                cells.append(button)
            self.buttons.append(cells)
        self.stats = tk.StringVar(value='')
        tk.Label(root, textvariable=self.stats, font=('Arial', 10),
                 bg='#172033', fg='#b9c5d8').pack(pady=12)
        tk.Button(root, text='New game', font=('Arial', 12),
                  command=self.new_game).pack(pady=(0, 22), ipadx=20, ipady=5)
        root.protocol('WM_DELETE_WINDOW', self.close)
        self.new_game()

    def new_game(self):
        if self.pending_move is not None:
            self.root.after_cancel(self.pending_move)
            self.pending_move = None
        self.board = TicTacToeBoard()
        self.agent = TicTacToeMinimaxAgent(self.board)
        self.thinking = False
        self.stats.set('')
        self.refresh()

    def refresh(self):
        for row in range(3):
            for col in range(3):
                symbol = self.board[row][col]
                disabled = self.board.game_over or self.thinking or symbol != ' '
                self.buttons[row][col].configure(
                    text=symbol, state=tk.DISABLED if disabled else tk.NORMAL,
                    disabledforeground='#2458a6' if symbol == 'X' else '#ad462b')
        winner = self.board.check_winner()
        if winner == 'Draw':
            self.status.set("It's a draw!")
        elif winner:
            self.status.set('You win!' if winner == 'X' else 'Minimax wins!')
        else:
            self.status.set('Minimax is thinking…' if self.thinking else 'Your turn — choose a square')

    def human_move(self, row, col):
        if self.thinking or self.board.game_over or self.board[row][col] != ' ':
            return
        self.board.make_move(row, col)
        if not self.board.game_over:
            self.thinking = True
            self.pending_move = self.root.after(80, self.computer_move)
        self.refresh()

    def computer_move(self):
        self.pending_move = None
        try:
            move = self.agent.get_next_move()
            if move is not None:
                self.board.make_move(*move)
            self.stats.set(f'Search nodes: {self.agent.nodes_expanded:,}')
        finally:
            self.thinking = False
            self.refresh()

    def close(self):
        if self.pending_move is not None:
            self.root.after_cancel(self.pending_move)
        self.root.destroy()
