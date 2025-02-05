
class game():
    
    def __init__(self):
        self.tictactoe = [[".",".","."],[".",".","."],[".",".","."]]

    
    def tictactoechoice(self,xy,player):
        self.tictactoe[xy[0]][xy[1]] = player
        

    
test = game()
test.tictactoechoice((0,0),"X")
print(test.tictactoe)