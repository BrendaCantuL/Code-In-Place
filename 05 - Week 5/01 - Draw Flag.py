from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_flag(canvas)

def draw_flag(canvas):
    # Draw the red top half of the flag
    red_rect = canvas.create_rectangle(
        0,                  # left_x
        0,                  # top_y
        CANVAS_WIDTH,       # right_x
        CANVAS_HEIGHT / 2,  # bottom_y
        "red"               # color (positional argument)
    )

if __name__ == '__main__':
    main()
