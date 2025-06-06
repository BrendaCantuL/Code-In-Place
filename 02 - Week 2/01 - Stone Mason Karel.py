from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def put_Stone():
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
    turn_right()
    move_forward()
    turn_right()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
    turn_left()
    move_forward()
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
    turn_right()
    move_forward()
    turn_right()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
    turn_left()
def move_forward():
    for i in range(4):
        move()
def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    put_Stone()

if __name__ == '__main__':
    main()