import random
import time
from curses import wrapper,newpad,newwin

class board:
    def __init__(self,r,c,seed=42) -> None:
        self.rows=r
        self.cols=c
        self.seed=seed
        self.state=[[0 for _ in range(self.cols)]for _ in range(self.rows)]
    
    def soupifier(self):
        self.state=[[
            self.randfiller(i,j) for i in range(self.cols)]
            for j in range(self.rows)
        ]
    
    def randfiller(self,r,c):
        s=(r*self.seed)+c
        random.seed(s)
        return random.randint(0,1)
    
    def print(self,stdscr):
        c=0
        for i in range(self.rows):
            st=''
            for j in range(self.cols):
                if self.state[i][j]==1: st+=' * '
                else: st+=' - '
            #st+='|'     
            stdscr.addstr(c,0,st)
            c+=1
            
    def update(self):
        new=board(self.rows,self.cols,self.seed)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.state[i][j]==1: 
                    if self.nbcount(i,j)<2 or self.nbcount(i,j)>3:
                        self.state[i][j]==0
                elif self.state[i][j]==0 and self.nbcount(i,j)==3:
                        self.state[i][j]==1
    
    def nbcount(self,i,j):
        count=0
        if i==0:
            if j==0:
                count+=self.state[i][j+1]+self.state[i+1][j+1]+self.state[i+1][j]
            if j== self.cols-1:
                count+=self.state[i][j-1]+self.state[i+1][j-1]+self.state[i+1][j]
            else:
                count+=self.state[i][j-1]+self.state[i][j+1]+self.state[i+1][j]+self.state[i+1][j-1]+self.state[i+1][j+1]
        elif i==self.rows-1:
            if j==0:
                count+=self.state[i-1][j]+self.state[i-1][j+1]+self.state[i][j+1]
            if j==self.cols-1:
                count+=self.state[i-1][j]+self.state[i-1][j-1]+self.state[i][j-1]
            else:
                count+=self.state[i][j-1]+self.state[i][j+1]+self.state[i-1][j]+self.state[i-1][j-1]+self.state[i-1][j+1]
        else:
            count+=self.state[i+1][j]+self.state[i+1][j+1]+self.state[i+1][j-1]+self.state[i][j+1]+self.state[i][j-1]+self.state[i-1][j]+self.state[i-1][j-1]+self.state[i-1][j+1]
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
        stdscr.refresh()
        time.sleep(1)
        obj.update()
        
        
        key=stdscr.getch()
        if key==ord('q'):
            break

wrapper(main)