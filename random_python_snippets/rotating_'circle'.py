import curses
import math
import time


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    height, width = stdscr.getmaxyx()
    y = height // 2
    x = width // 2

    for i in range(360):
        stdscr.clear()
        for j in range(0, 1080, 30):
            char_y = int(y + (math.sin(math.radians(j + i)) * (height // 4)))
            char_x = int(x + (math.cos(math.radians(j + i)) * (width // 4)))
            stdscr.addstr(char_y, char_x, "- 🟢  🟢 🟢  -", curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.0018)


curses.wrapper(main)
