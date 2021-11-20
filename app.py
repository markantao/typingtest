# Imports
import curses
from curses import wrapper
import time

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
    start_time = time.time()
    stdscr.nodelay(True) # Do not wait for the user to click a key (for wpm)


#Typing Characters
    while True:
        time_elapsed = max(time.time() - start_time, 1) #calculating time
        # We use "max" and "1" so that we don't get a division by 1 error
        # Explain division by 1 error in readme.md
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) # The average word is 5 characters
        # wpm "algorithm" above.
        # We round the "algorithm" so that we don't get a decimal number but rather a whole number
        #explain "algorith" in readme.md

# Explain all the things that I learnt in the readme.md such as division by 1 error and the "algorith" for wpm and such

        stdscr.clear() # Clears terminal
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh() # Refresh terminal to show changes

        # Finishing the game
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        #Making sure that line 57 won't crash, if it does, the continue keyword will bring us back 
        # to the start of the while loop and it skips from line 66 as you cannot check what key was
        # was pressed if no key was pressed. (Has no value)

        try:
            key = stdscr.getkey() # This is known as a block; kind of like an input
        except:
            continue

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
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)