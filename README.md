# Tic-Tac-Toe Minimax Agent

A Python tic-tac-toe game with a minimax AI opponent and a clickable Tkinter interface.

You play **X**, and the AI plays **O**. The agent explores every possible continuation and chooses the best move, assuming both players play optimally. Try to force a draw—you can’t beat it!

## Features

- Full minimax search
- Graphical board with a New Game button
- Search-node counter
- Optional terminal mode
- No third-party Python packages required

## Run

Requires Python 3.10+ with Tkinter installed.

Clone the repository, open the project folder, and run:

```bash
python main.py
```

For terminal mode:

```bash
python main.py --console
```

On Windows, you can use `py` instead of `python`; on macOS/Linux, use `python3` if needed.

## Project structure

- `main.py` — application launcher
- `tictactoe/agent.py` — minimax algorithm
- `tictactoe/board.py` — board state and game rules
- `tictactoe/gui.py` — graphical interface
- `tictactoe/console.py` — terminal interface
