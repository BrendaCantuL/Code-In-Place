from karel.stanfordkarel import *

def main():
    put_checker_row_starting_with_beeper()
    while front_is_clear():
        if facing_east():
            turn_left()
        else:
            turn_right()
        if front_is_clear():
            move()
            if facing_north():
                turn_right()
            else:
                turn_left()
            check_below_and_fill()
        else:
            if facing_north():
                turn_right()
            else:
                turn_left()
    return_home()

def check_below_and_fill():
    turn_around()
    move()
    if beepers_present():
        turn_around()
        move()
        put_checker_row_starting_with_space()
    else:
        turn_around()
        move()
        put_checker_row_starting_with_beeper()

def put_checker_row_starting_with_beeper():
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def put_checker_row_starting_with_space():
    if front_is_clear():
        move()
        put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def return_home():
    while not_facing_south():
        turn_left()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    while not_facing_east():
        turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()