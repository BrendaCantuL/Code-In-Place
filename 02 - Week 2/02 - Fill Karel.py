from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def f1():
    while(front_is_clear() and no_beepers_present()):
        put_beeper()
        move()
    put_beeper()
    turn_left()
    turn_left()
    while(front_is_clear() ):
        move()
    turn_right()
    while(front_is_clear()):
        if front_is_clear():
            move()
            turn_right()
            while(front_is_clear() and no_beepers_present()):
                put_beeper()
                move()
            put_beeper()
            turn_left()
            turn_left()
            while(front_is_clear() ):
                move()
            turn_right()
        if front_is_blocked() :
            turn_right()
            while(front_is_clear()):
                move()
    
        
def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    f1()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()