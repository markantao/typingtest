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

#Overlaying Text
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target) # Adds the target text
    stdscr.addstr(1, 0, f"WPM: {wpm}") # Adds the WPM

    # for every character typed, change color to Yellow as dictated on line 25.
    #enumerate is going to give us the element from our current text as well as the index in the list
    #Overlaying Text
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


#Typing Screen
def wpm_test(stdscr):
    target_text = "Hello World, this is an example text!"
    current_text = []
    wpm = 0


#Typing Characters
    while True:

        stdscr.clear() # Clears terminal
        display_text(stdscr, target_text, current_text, wpm)
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
        # Making sure we can't type more characters than needed
        elif len(current_text) < len(target_text):
            current_text.append(key) # appends every key pressed to "current_text" list




# Initializing Colors and Running App
def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)