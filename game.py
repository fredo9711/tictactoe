
import numpy as np
class game():
    
    def __init__(self):
       # self.tictactoe = [["","",""],["","",""],["","",""]]
       self.tictactoe = np.full((3,3),"",dtype=str)

    
    def tictactoeupdate(self,xy,player):
        self.tictactoe[xy[0]][xy[1]] = player

    """def linecheck(self,player1,player2):
        for i in range(len(self.tictactoe)):
            if self.tictactoe[i] == [player1,player1,player1]:
                return player1
        return ""
    """
    def linecheck(self,player1,player2):
        if np.any(np.all(self.tictactoe == player1,axis=1)):
            return player1
        if np.any(np.all(self.tictactoe == player2,axis=1)):
            return player2
        return ""

    def colonmcheck(self,player1,player2):
        if np.any(np.all(self.tictactoe.T == player1,axis=1)):
            return player1
        if np.any(np.all(self.tictactoe.T == player2,axis=1)):
            return player2
        return ""

    def diagcheck(self,player1,player2):
        if np.all(np.diag(self.tictactoe) == player1):
            return player1
        elif np.all(np.diag(self.tictactoe) == player2):
            return player2
        if np.all(np.diag(np.fliplr(self.tictactoe)) == player1):
            return player1
        elif np.all(np.diag(np.fliplr(self.tictactoe)) == player2):
            return player2
        return ""


    def wincheck(self,player1,player2):
        pass



        

    
test = game()
test.tictactoeupdate((0,0),"X")
print(test.tictactoe)
print(len(test.tictactoe))