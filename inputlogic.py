class inputlogic():
    
    def __init__(self,player):
        self.player = player
    
    def matrixcheck(self,matrix,xy):
        pass
    def tupleconversion(self,input):
        pass
    def inputcheck(self,matrix):
        userinput = input("Write the coordonnate xy ( numbers between 0-2) 01 for example : ")
        if len(userinput)==2 and userinput.isdigit():
            return True
        return False
        
    def input(self,matrix):
        while(True):
           userinput = self.inputcheck(matrix)
           if userinput: return userinput



            
