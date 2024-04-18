import random

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
    
    def print(self):
        for i in range(self.rows):
            temp=[]
            for j in range(self.cols):
                temp.append(self.state[i][j])
            print(temp)
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
    obj=board(10,10)
    obj.print()

