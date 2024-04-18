import random
import time
from curses import wrapper,newpad,newwin

class board:
    def __init__(self,r,c,seed=42) -> None:
        self.rows=r
        self.cols=c
        self.seed=seed
        self.state=[[
            self.randfiller(i,j) for i in range(self.cols)]
            for j in range(self.rows)
        ]
    
    def randfiller(self,r,c):
        s=(r*self.seed)+c
        random.seed(s)
        return random.randint(0,1)
    
    def print(self,stdscr):
        r=0
        for i in range(self.rows):
            st=''
            for j in range(self.cols):
                if self.state[i][j]==1: st+=' * '
                else: st+=' - '
            #st+='|'     
            stdscr.addstr(r,0,st)
            r+=1
            
    def update(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.state[i][j]==1: 
                    if self.nbcount(i,j)<2 or self.nbcount(i,j)>3:
                        self.state[i][j]==0
                elif self.state[i][j]==0 and self.nbcount(i,j)==3:
                    self.state[i][j]==1
    
    def nbcount(self,i,j):
        count=0
        
        return count


def main(stdscr):
    '''
        TODO:
        1.  Build a data structure to store the board state
        2.  “Pretty-print” the board to the terminal
        3.  Given a starting board state, calculate the next one
            - update and refresh/print
        4.  Run the game forever
        RULES:
        1. live && count<2 == dead 
        2. live && count==2 OR 3 == live
        3. live && count>3 == dead
        4. dead && count == 3 == live
        ANCILLARY:
        1. filesaving mechanism 
        2. make a terminal ui
        3. config files for rules 
    '''
    obj=board(10,10)
    while True:
        stdscr.clear()
        obj.print(stdscr)
        obj.update()
        #time.sleep(1)
        stdscr.refresh()
        key=stdscr.getch()
        if key==ord('q'):
            break

wrapper(main)