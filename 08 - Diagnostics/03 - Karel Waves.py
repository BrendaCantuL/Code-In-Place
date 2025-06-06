from karel.stanfordkarel import *

def main():
    # Start in column 2, first triangle
    for _ in range(4):
        draw_wave()
        if front_is_clear():
            move_to_next_wave()

def draw_wave():
    put_beeper()        # base of triangle
    turn_left()
    move()
    put_beeper()        # left side
    turn_right()
    move()
    put_beeper()        # right side
    turn_right()
    move()
    turn_left()         # reposition to base row, facing East

def move_to_next_wave():
    if front_is_clear():
        move()
    if front_is_clear():
        move()

def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == '__main__':
    main()
