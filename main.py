import random

class board:
    def __init__(self,r,c,seed=42) -> None:
        self.rows=r
        self.cols=c
        self.seed=seed
        self.state=[[
            self.randfiller(i,j,seed) for i in range(self.cols)]
            for j in range(self.rows)
        ]
    
    def randfiller(self,r,c):
        random.seed((r*self.seed)+c)
        return random.randint(0,1)
    
    def print():
        pass

if __name__=="__main__":
    '''
        TODO:
        1.  Build a data structure to store the board state
            -started 1:36 4/18
        2.  “Pretty-print” the board to the terminal
        3.  Given a starting board state, calculate the next one
        4.  Run the game forever
        ANCILLARY:
        1. filesaving mechanism 
        2. make a terminal ui
        3. config files for rules 
    '''
    print("Hello")

