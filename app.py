# Imports
import curses
from curses import wrapper

#Starting Screen
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Speed Typing Test")
    stdscr.addstr("\nBy: Mark Antao")
    stdscr.refresh()
    stdscr.getkey()


#Typing Screen
def wpm_test(stdscr):
    target_text = "Hello World, this is an example text!"
    current_text = []


#Typing Characters
    while True:

        stdscr.clear() # Clears terminal
        stdscr.addstr(target_text) # Adds the target text


        # for every character typed, change color to Yellow as dictated on line 25.
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh() # Refresh terminal to show changes

        key = stdscr.getkey()

        # The ordinal (ord) value of a key is its numerical value on the keyboard
        #ASCII 27 == Escape Key

#Deleting Characters
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"): # Different backspace representations for different OS'
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key) # appends every key pressed to "current_text" list




# Initializing Colors and Running App
def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)