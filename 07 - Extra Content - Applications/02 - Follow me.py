from graphics import Canvas
import time

CANVAS_SIZE = 400
BALL_DIAMETER = 50
PAUSE_TIME = 1 / 50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    ball = canvas.create_oval(
        0, 0,
        BALL_DIAMETER,
        BALL_DIAMETER,
        'blue'
    )

    radius = BALL_DIAMETER // 2

    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # Center the ball on the mouse position
        new_x = mouse_x - radius
        new_y = mouse_y - radius
        canvas.moveto(ball, new_x, new_y)

        time.sleep(PAUSE_TIME)
        print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")

if __name__ == '__main__':
    main()
