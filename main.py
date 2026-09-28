"""Run with: python main.py (or python main.py --console)."""
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Play X against a minimax O opponent.")
    parser.add_argument('--console', action='store_true', help='Play in the terminal instead of a window.')
    args = parser.parse_args()
    if args.console:
        from tictactoe.console import play
        play()
        return 0
    try:
        import tkinter as tk
        from tictactoe.gui import TicTacToeApp
    except ImportError:
        print('Tkinter is unavailable. Install Python with Tk support, or run: python main.py --console', file=sys.stderr)
        return 1
    try:
        root = tk.Tk()
    except tk.TclError as error:
        print(f'Could not open a window: {error}\nTry: python main.py --console', file=sys.stderr)
        return 1
    TicTacToeApp(root)
    root.mainloop()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
