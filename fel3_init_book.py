import curses
import time

menu = ['View Balance','Make Deposit','Withdrawal','Exit']

def menu_display(stdscr,selected_row_index):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for index, opt in enumerate(menu):
        x = w //2 - len(opt)//2
        y = h//2 - len(menu)//2 + index
        if index == selected_row_index:
            curses.init_pair(3,curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_GREEN)
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(y, x, opt)
            stdscr.attroff(curses.color_pair(2))
        else:
            stdscr.addstr(y, x, opt)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    current_row_index = 0
    menu_display(stdscr, current_row_index)


    while True:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_index > 0:
            current_row_index -= 1
            stdscr.refresh()
        elif key == curses.KEY_DOWN and current_row_index < len(menu) - 1:
            current_row_index += 1
            stdscr.refresh()
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, 'you pressed {}'.format(menu[current_row_index]))
            ###

            



            ###
            stdscr.refresh()
            stdscr.getch()

        menu_display(stdscr, current_row_index)

        stdscr.refresh()
    curses.init_pair(3,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_GREEN)
    #time.sleep(3)
curses.wrapper(main)