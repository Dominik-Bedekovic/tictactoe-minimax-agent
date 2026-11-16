"""Compare minimax with and without alpha-beta pruning.

Run with: python benchmark.py
"""
from tictactoe.board import TicTacToeBoard
from tictactoe.agent import TicTacToeMinimaxAgent

OPENINGS = [("corner", (0, 0)), ("edge", (1, 0)), ("centre", (1, 1))]


def run(opening, pruning):
    """Search O's reply to X's opening; return (nodes, milliseconds)."""
    board = TicTacToeBoard()
    board.make_move(*opening)
    agent = TicTacToeMinimaxAgent(board, random_chance=0, is_benchmark=True, is_prune=pruning)
    agent.get_next_move()
    return agent.num_of_searches, agent.elapsed_time


print(f"{'Opening':<10}{'Pruning':<10}{'Nodes':>10}{'Time (ms)':>12}")
for name, opening in OPENINGS:
    nodes_off, ms_off = run(opening, pruning=False)
    nodes_on, ms_on = run(opening, pruning=True)
    print(f"{name:<10}{'off':<10}{nodes_off:>10,}{ms_off:>12.1f}")
    print(f"{name:<10}{'on':<10}{nodes_on:>10,}{ms_on:>12.1f}")
    print(f"  -> pruning searched {1 - nodes_on / nodes_off:.1%} fewer nodes\n")
