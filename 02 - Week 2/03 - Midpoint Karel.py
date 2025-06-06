from karel.stanfordkarel import *

def main():
    mark_walls()
    put_beepers_down()
    turn_around()
    move()
    put_beeper()  # ← This is the *only* one that places the final midpoint beeper
    turn_around()
    go_to_wall()
    turn_around()
    last_beeper_standing()
    go_to_midpoint()

def mark_walls():
    go_to_wall()
    put_beeper()
    turn_around()
    go_to_wall()
    put_beeper()
    turn_around()
    move()

def go_to_wall():
    while front_is_clear():
        move()

def put_beepers_down():
    while no_beepers_present():
        move()
        if beepers_present():
            turn_around()
            move()
            put_beeper()
            move()

def last_beeper_standing():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    if beepers_present():
        pick_beeper()

def go_to_midpoint():
    turn_around()
    while no_beepers_present():
        move()
    # Karel is now on the midpoint
    while not_facing_east():
        turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()