from karel.stanfordkarel import *

# File: cleanup.py
# -----------------------------
# Karel picks up all beepers on the first row.

def main():
    while front_is_clear():
        pick_beepers_here()
        move()
    # One last time in case there's a beeper on the last square
    pick_beepers_here()

# Helper function to pick up all beepers on one square
def pick_beepers_here():
    while beepers_present():
        pick_beeper()

# don't edit these next two lines
if __name__ == '__main__':
    main()
