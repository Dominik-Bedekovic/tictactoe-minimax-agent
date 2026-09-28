# Tic-Tac-Toe Minimax

A standalone Python game. You play X; the minimax agent plays O. Full minimax explores every continuation and chooses the lowest score: X win = +1, draw = 0, O win = -1. Equally good moves are chosen in row-major order. The agent cannot be beaten from the starting position with these rules.

## Run

Extract the ZIP. Open a terminal in the extracted `tictactoe-minimax` folder.

Windows:

```sh
py main.py
```

macOS/Linux:

```sh
python3 main.py
```

`python main.py` also works if `python` is your Python 3 command. Python 3.10 or newer is recommended. The graphical board uses Tkinter. No pip dependencies, NumPy, Matplotlib, Jupyter, or ipywidgets are required.

On Windows, use a Python installation with Tcl/Tk support. If the window cannot open, run `py main.py --console`. On Ubuntu/Debian, Tkinter is normally supplied by `python3-tk`. When using WSL without a graphical desktop, use console mode or run with Windows Python.

Click an empty square to play. The computer responds automatically. New game resets the board; the search-node counter shows the most recent AI search. A short pause on the first search is normal: this is the full minimax algorithm, without alpha-beta pruning or caching.

The recommended entry point is **main.py**. In an editor such as VS Code, open the whole project folder and run that file. Running from a terminal makes any error messages easy to read. The package files are imported by the launcher and should not be run individually.

## Files

- `main.py`: launcher, GUI/console selection.
- `tictactoe/board.py`: board state, valid moves, wins and draws.
- `tictactoe/agent.py`: corrected minimax agent.
- `tictactoe/gui.py`: clickable Tkinter interface.
- `tictactoe/console.py`: terminal interface.
- `tests/test_agent.py`: exhaustive move-selection checks.

## Corrections to the notebook code

- Call methods as `self.minimax(...)`, not `minimax(self, ...)`.
- Return `bestScore` consistently instead of the undefined `best_score`. The original variable names, comments, and separate X/O branches are preserved.
- Initialize the minimizing move search with positive infinity so it still selects a legal move when every move loses. The supplied reference implementation had this edge-case bug too.
- Initialize the node counter in the constructor and reset it for each move search.
- Undo each simulated move after evaluating it, as in the original code; normal search preserves the real turn and game-over flag.
- Import the board explicitly. Separate the Jupyter interface from the standalone application.

The agent plays O and should be called on O's turn. `get_next_move()` returns a `(row, column)` tuple, or `None` if the game has already ended. The game applies the chosen move using `board.make_move(...)`.

## Tests

```sh
python -m unittest discover -s tests -v
```

The exhaustive test checks all 2,097 reachable unfinished O-turn positions against an independent solver, including forced losses, and checks that searching preserves the board. GUI display requires a local desktop; it was not visually tested in the preparation environment.
