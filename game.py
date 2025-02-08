
import numpy as np
from ailogic import ailogic
from inputlogic import inputlogic
class game:
    
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
        out =self.linecheck(player1,player2)+self.colonmcheck(player1,player2)+self.diagcheck(player1,player2)
        return out[0] if len(out) >0 else ""
    
    def drawcheck(self):
        return np.all(self.tictactoe !="")


    def aivsplayer(self):
        player1 = ailogic("X")
        player2=inputlogic("O")
        playertab = [player1,player2]
        
        if np.random.randint(0,2) ==1:
            playertab =list(reversed(playertab))
        
        while(True):
            for player in playertab:
                print(self.tictactoe)
                self.tictactoeupdate(player.inputcheck(self.tictactoe),player.player)
                
                print(self.drawcheck())
                if self.drawcheck():
                    print("Match nul")
                    return "Match nul"
                
                win = self.wincheck(playertab[0].player,playertab[1].player)
                print(win)
                if win !="": return " le Vainqueur est le joueur "+win

        
        


