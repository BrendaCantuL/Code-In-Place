from graphics import Canvas
import random
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 600
BRICK_ROWS = 10
BRICK_COLS = 10
BRICK_WIDTH = 36
BRICK_HEIGHT = 10
BRICK_SPACE = 4
TOP_OFFSET = 50
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
PADDLE_Y_OFFSET = 50
BALL_DIAMETER = 20
BALL_RADIUS = BALL_DIAMETER // 2
TURNS = 3
PAUSE_TIME = 1 / 100

BRICK_COLORS = ['red', 'red', 'orange', 'orange', 'yellow', 'yellow', 'green', 'green', 'cyan', 'cyan']

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    bricks = create_bricks(canvas)
    total_bricks = len(bricks)

    paddle = create_paddle(canvas)
    ball = create_ball(canvas)

    for turn in range(TURNS):
        reset_ball(canvas, ball)
        change_x = random.choice([-4, 4])
        change_y = 4
        while True:
            move_paddle(canvas, paddle)
            canvas.move(ball, change_x, change_y)
            bx = canvas.get_left_x(ball)
            by = canvas.get_top_y(ball)
            ball_right = bx + BALL_DIAMETER
            ball_bottom = by + BALL_DIAMETER

            # Bounce off walls
            if bx <= 0 or ball_right >= CANVAS_WIDTH:
                change_x = -change_x
            if by <= 0:
                change_y = -change_y

            # Check for bottom (lose turn)
            if ball_bottom >= CANVAS_HEIGHT:
                break

            # Check for collisions
            collided = canvas.find_overlapping(bx, by, ball_right, ball_bottom)
            for obj in collided:
                if obj == ball:
                    continue
                if obj == paddle:
                    change_y = -abs(change_y)
                    break
                elif obj in bricks:
                    canvas.delete(obj)
                    bricks.remove(obj)
                    total_bricks -= 1
                    change_y = -change_y
                    break

            if total_bricks == 0:
                canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, text='You Win!', font='30px Arial', color='green')
                canvas.mainloop()
                return

            time.sleep(PAUSE_TIME)

    canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, text='Game Over', font='30px Arial', color='red')
    canvas.mainloop()

def create_bricks(canvas):
    bricks = []
    start_x = (CANVAS_WIDTH - (BRICK_COLS * BRICK_WIDTH + (BRICK_COLS - 1) * BRICK_SPACE)) // 2
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            x = start_x + col * (BRICK_WIDTH + BRICK_SPACE)
            y = TOP_OFFSET + row * (BRICK_HEIGHT + BRICK_SPACE)
            color = BRICK_COLORS[row % len(BRICK_COLORS)]
            brick = canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT, color)
            bricks.append(brick)
    return bricks

def create_paddle(canvas):
    x = (CANVAS_WIDTH - PADDLE_WIDTH) // 2
    y = CANVAS_HEIGHT - PADDLE_Y_OFFSET
    return canvas.create_rectangle(x, y, x + PADDLE_WIDTH, y + PADDLE_HEIGHT, 'black')

def move_paddle(canvas, paddle):
    mouse_x = canvas.get_mouse_x()
    if mouse_x is not None:
        new_x = mouse_x - PADDLE_WIDTH // 2
        new_x = max(0, min(new_x, CANVAS_WIDTH - PADDLE_WIDTH))
        canvas.moveto(paddle, new_x, CANVAS_HEIGHT - PADDLE_Y_OFFSET)

def create_ball(canvas):
    x = CANVAS_WIDTH // 2 - BALL_RADIUS
    y = CANVAS_HEIGHT // 2 - BALL_RADIUS
    return canvas.create_oval(x, y, x + BALL_DIAMETER, y + BALL_DIAMETER, 'blue')

def reset_ball(canvas, ball):
    x = CANVAS_WIDTH // 2 - BALL_RADIUS
    y = CANVAS_HEIGHT // 2 - BALL_RADIUS
    canvas.moveto(ball, x, y)
    time.sleep(1)  # Pause before starting turn

if __name__ == '__main__':
    main()
