from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

DELAY = 0.1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    score = 0
    current_delay = DELAY

    border_x = CANVAS_WIDTH - SIZE
    border_y = CANVAS_HEIGHT - SIZE

    # Create player
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, 'blue')
    player_x = canvas.get_left_x(player)
    player_y = canvas.get_top_y(player)

    # Create goal
    goal_x = 360
    goal_y = 360
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE, 'red')

    # Score display
    score_display = canvas.create_text(200, 10, text=f"Score: {score}", font='20px Arial')

    direction = 'Right'
    border_reached = False

    while True:
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft' and direction != 'Right':
            direction = 'Left'
        if key == 'ArrowRight' and direction != 'Left':
            direction = 'Right'
        if key == 'ArrowUp' and direction != 'Down':
            direction = 'Up'
        if key == 'ArrowDown' and direction != 'Up':
            direction = 'Down'

        if direction == 'Left':
            canvas.move(player, -SIZE, 0)
            player_x -= SIZE
        if direction == 'Right':
            canvas.move(player, SIZE, 0)
            player_x += SIZE
        if direction == 'Up':
            canvas.move(player, 0, -SIZE)
            player_y -= SIZE
        if direction == 'Down':
            canvas.move(player, 0, SIZE)
            player_y += SIZE

        time.sleep(current_delay)

        if player_x == goal_x and player_y == goal_y:
            score += 1
            canvas.change_text(score_display, f"Score: {score}")
            current_delay = max(0.02, current_delay - 0.005)

            while True:
                goal_x = 20 * random.randint(0, 19)
                goal_y = 20 * random.randint(0, 19)
                if goal_x != player_x or goal_y != player_y:
                    break

            canvas.delete(goal)
            goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE, 'red')

        if player_x >= border_x or player_y >= border_y or player_x < 0 or player_y < 0:
            border_reached = True
            break

    if border_reached:
        canvas.create_text(200, 200, text='GAME OVER', font='30px Arial', color='black')
        canvas.create_text(200, 230, text=f'Score: {score}', font='20px Arial', color='gray')
        print(score)
        print('You just crossed the line!')

    canvas.mainloop()

if __name__ == '__main__':
    main()
