# typingtest
## By: Mark Antao
This project is created completely in python and uses a number for modules to run.
I learned a lot of new things in this project and a detailed summary of the project will be below which includes an overview of the project, what I learned, and how to run it on your own machine.

> **Overview of the Project**

Typing Test is a terminal run typing game which tests your typing skills by giving you random text and testing your typing speed by using a "words per minute" algorithm. This project used modules such as **curses**, **random**, and **time**. This project also uses a txt file to generate the random text. This is an overview of the project.

> **What I Learned**

This project was created in Python, by using the curses module. I have never used the curses module before which resulted in me learning a lot of things. Firstly, the basic "commands" in curses such as:
- **stdscr.clear()** (Clears the terminal) 
- **stdscr.addstr()** (Allows you to add a string)
- **stdscr.refresh()** (Allows you to refresh the terminal)
- **stdscr.getkey()** (Gets a key, but returns a string rather than an integer)

I also learned about the wpm algorithm:

**WPM Algorithm**
This algorithm is beneficial to the project as it allows the computer to judge how fast a person is typing.
The algorithm goes as follows:

***wpm = round((len(current_text) / (time_elapsed / 60)) / 5)***

This algorithm takes the number of characters that the user types _(len(current\_text))_, and divides it by the time elapsed of the users typing divided by 60 as there are 60 seconds in a minute _(time\_elapsed / 60)_. It then takes this value and divides it by 5 as the average word is 5 letters. _) / 5)_

This is an overview of what I learned through building this project.

> **How to Run**

This project is really fun to play around with as you can test your typing speed with multiple different text strings to use and it is really easy to use. Here is how to run it on your machine:

***Prerequisites***
- Python installed
- Clone of this repository

If you have everything checked above, you are ready to run this project! Open your terminal and cd into the directery containing the files used for this project (app.py, randomtext.txt). Next, based on your os, you will either run one of these two commands for mac or windows os.

- ***python3 app.py*** - Mac and Linux
- ***python app.py*** - Windows

The game will startup and you can start playing! This is how you can run the project!
Steps in order will be posted below to reference quickly:

- Clone repository from [github repository](https://github.com/markantao/typingtest)
- Open your terminal and cd into the directory containing the cloned files
- Run one of the following commands listed above based on your OS
- Have Fun!
