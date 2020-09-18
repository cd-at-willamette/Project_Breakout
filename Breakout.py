# File: Breakout.py

"""
This program (once you have finished it) implements the Breakout game
"""

from pgl import GWindow, GOval, GRect, GState
import random

# Constants
GWINDOW_WIDTH = 360
GWINDOW_HEIGHT = 600
N_ROWS = 10
N_COLS = 10
BRICK_ASPECT_RATIO = 4 / 1
BRICK_TO_BALL_RATIO = 3 / 1  
BRICK_TO_PADDLE_RATIO = 2 / 3
BRICK_SEP = 2
TOP_FRACTION = 0.1
BOTTOM_FRACTION = 0.05
N_BALLS = 3
TIME_STEP = 10
INITIAL_Y_VELOCITY = 3.0
MIN_X_VELOCITY = 1.0
MAX_X_VELOCITY = 3.0

# Derived Constants
BRICK_WIDTH = (GWINDOW_WIDTH - (N_COLS + 1) * BRICK_SEP) / N_COLS
BRICK_HEIGHT = BRICK_WIDTH / BRICK_ASPECT_RATIO
PADDLE_WIDTH = BRICK_WIDTH / BRICK_TO_PADDLE_RATIO
PADDLE_HEIGHT = BRICK_HEIGHT / BRICK_TO_PADDLE_RATIO
PADDLE_Y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT - PADDLE_HEIGHT
BALL_SIZE = BRICK_WIDTH / BRICK_TO_BALL_RATIO


# Function: breakout
def breakout():
    """The main program for the Breakout game."""

    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gs = GState()

    # You fill in the rest of this function along with any additional
    # helper and callback functions you need






# Startup code
if __name__ == "__main__":
    breakout()
