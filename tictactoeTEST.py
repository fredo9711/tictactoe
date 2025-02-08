import unittest
import start
import game
import ailogic
import inputlogic


class tictactoeTEST(unittest.TestCase):

# Game test function
    def tictactoeupdate_test(self):
        pass

    def linecheck_test(self):
        board = [[1, 1, 1],
                 [0, 2, 0],
                 [2, 0, 2]]
        testgame = game()
        testgame.tictactoe = board
        self.assertEqual(testgame.linecheck(1,2),1)

    def colonmcheck_test(self):
        board = [[0, 1, 1],
                 [0, 2, 1],
                 [2, 0, 1]]
        testgame = game()
        testgame.tictactoe = board
        self.assertEqual(testgame.colonmcheck(1,2),1)
    
    def diagcheck_test(self):
        board1 = [[0, 1, 2],
                 [0, 2, 1],
                 [2, 0, 1]]
        testgame = game()
        testgame.tictactoe = board1
        self.assertEqual(testgame.diagcheck(1,2),2)
        board1 = [[1, 1, 2],
                 [0, 1, 1],
                 [2, 0, 1]]
        self.assertEqual(testgame.diagcheck(1,2),1)       
        

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
