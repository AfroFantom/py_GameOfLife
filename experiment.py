from curses import wrapper,newwin,newpad

def main(stdscr):
    pad=newpad(10,10)
    for y in range(10):
        for x in range(10):
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
    pad.refresh(0,0,10,10,50,85)
wrapper(main)