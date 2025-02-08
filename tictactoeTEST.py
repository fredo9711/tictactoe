import unittest
import start
from game import game
from ailogic import ailogic
from inputlogic import inputlogic


class tictactoeTEST(unittest.TestCase):

# Game test function
    def tictactoeupdate_test(self):
        pass

    def linecheck_test(self):
        testgame = game()
        testgame.tictactoe[0, 0] = "X"
        testgame.tictactoe[0, 1] = "X"
        testgame.tictactoe[0, 2] = "X"
        self.assertEqual(testgame.linecheck("X","O"),"X")

    def colonmcheck_test(self):
        testgame = game()
        testgame.tictactoe[0, 2] = "X"
        testgame.tictactoe[1, 2] = "X"
        testgame.tictactoe[2, 2] = "X"
        self.assertEqual(testgame.colonmcheck("X","O"),"X")
    
    def diagcheck_test(self):
        testgame = game()
        testgame.tictactoe[0, 0] = "X"
        testgame.tictactoe[1, 1] = "X"
        testgame.tictactoe[2, 2] = "X"
        self.assertEqual(testgame.diagcheck("X","O"),"X")
        testgame.tictactoe[0, 2] = "O"
        testgame.tictactoe[1, 1] = "O"
        testgame.tictactoe[2, 0] = "O"
        self.assertEqual(testgame.diagcheck("X","O"),"O")       
        

    def wincheck_test(self):
        pass

#AI logic
    def inputcheckai_test(self):
        pass

#Input logic
    def matrixcheck_test(self):
        pass

    def tupleconversion_test(self):
        pass

    def inputcheck_test(self):
        pass

    def input_test(self):
        pass



test = tictactoeTEST()
test.linecheck_test()
test.colonmcheck_test()
test.diagcheck_test()

