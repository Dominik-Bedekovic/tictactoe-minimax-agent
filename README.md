# Tic-Tac-Toe Minimax Agent

A Python tic-tac-toe game with a minimax AI opponent and a clickable Tkinter interface.

You play **X**, and the AI plays **O**. The agent explores every possible continuation and chooses the best move, assuming both players play optimally. Try to force a draw—you can’t beat it!

## Features

- Full minimax search
- Alpha-beta pruning
- Difficulty levels (Easy / Medium / Hard)
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

For testing you should install pytest through pip to run `test_agent.py` preferably with a virtual environment, then run:

```bash
python -m pytest
```

You can also run benchmarking through `benchmark.py`, to do so run:

```bash
python benchmark.py
```

On Windows, you can use `py` instead of `python`; on macOS/Linux, use `python3` if needed.

## Benchmark table

| Opening   | Pruning   | Nodes    | Time (ms)   |
| :-------: | :-------: | :------: | :---------: |
| corner    | off       | 59,704   |   83.5      |
| corner    | on        |  4,089   |    6.7      |

>pruning searched 93.2% fewer nodes


| Opening   | Pruning   | Nodes    | Time (ms)   |
| :-------: | :-------: | :------: | :---------: |
| edge      | off       | 63,904   |   89.6      |
| edge      | on        |  7,641   |   14.7      |

>pruning searched 88.0% fewer nodes

| Opening   | Pruning   | Nodes    | Time (ms)   |
| :-------: | :-------: | :------: | :---------: |
| centre    | off       | 55,504   |   108.8     |
| centre    | on        |  6,138   |    10.2     |

>pruning searched 88.9% fewer nodes

## Project structure

- `main.py` — application launcher
- `tictactoe/agent.py` — minimax algorithm
- `tictactoe/board.py` — board state and game rules
- `tictactoe/gui.py` — graphical interface
- `tictactoe/console.py` — terminal interface
- `benchmark.py` — benchmarking tool