import inputlogic
import numpy as np 
class ailogic(inputlogic):
    
    def __init__(self,player):
        self.player = player

    def inputcheck(self,matrix):
        while(True):
            x =np.random.randint(0,3)
            y =np.random.randint(0,3)
            if self.matrixcheck(matrix,(x,y)):
                return x,y

