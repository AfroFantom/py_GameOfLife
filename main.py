import random
import time

class board:
    def __init__(self,r,c,seed=42) -> None:
        self.rows=r
        self.cols=c
        self.seed=seed
        self.state=[[
            self.randfiller(i,j) for i in range(self.cols)]
            for j in range(self.rows)
        ]
    
    def statekiller(self):
        self.state=[[
            0 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def randfiller(self,r,c):
        s=(r*self.seed)+c
        random.seed(s)
        return random.randint(0,1)
    
    def update(self):
        new=board(self.rows,self.cols,self.seed)
        new.statekiller()
        for i in range(self.rows):
            for j in range(self.cols):
               new.state[i][j]=self.nextCellVal(i,j)
        return new
    
    def nextCellVal(self,i,j):
        count=self.nbcount(i,j)
        if self.state[i][j]==1:
            if count ==2 or count ==3:
                return 1
            else:
                return 0
        else:
            if count == 3:
                return 1
            else:
                return 0

    def nbcount(self,i,j):
        count=0
        for x in range((i-1),(i+1)+1):
                if x<0 or x>=self.rows:continue
                for y in range((j-1),(j+1)+1):
                    if y<0 or y>=self.cols:continue
                    if x==i or y==j: continue   
                    if self.state[x][y]==1:count+=1
       
        return count

                    
                    
def printbrd(board):
        for i in range(board.rows):
            st=''
            for j in range(board.cols):
                if board.state[i][j]==1: st+="\u2588" *2
                else: st+=' '*2
            st+='\n'     
            print(st)

        print("-"*board.cols)


if __name__ == "__main__":
    '''
        TODO:
        1. filesaving mechanism 
        2. make a terminal ui
        3. config files for rules
        4. finish nbcount
        5. https://https://robertheaton.com/2018/07/20/project-2-game-of-life/ for reference
    
        RULES:
        1. live && count<2 == dead 
        2. live && count==2 OR 3 == live
        3. live && count>3 == dead
        4. dead && count == 3 == live
        
         
    '''
    obj=board(100,50)
    while True:
        printbrd(obj)
        time.sleep(0.3)
        temp_obj=obj.update()
        obj=temp_obj