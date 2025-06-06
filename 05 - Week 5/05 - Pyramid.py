from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH = 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) / 2
        y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT

        for b in range(bricks_in_row):
            x1 = start_x + b * BRICK_WIDTH
            y1 = y
            x2 = x1 + BRICK_WIDTH
            y2 = y1 + BRICK_HEIGHT
            canvas.create_rectangle(x1, y1, x2, y2, "yellow", "black")

if __name__ == '__main__':
    main()
