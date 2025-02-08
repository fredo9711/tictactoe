class inputlogic:
    
    def __init__(self,player):
        self.player = player
    
    def __lt__(self,other):
        return self.player < other.player
    
    def matrixcheck(self,matrix,xy):
        return True if matrix[xy[0]][xy[1]] == "" else False
    
    def tupleconversion(self,input):
        return int(input[0]), int(input[1])
    
    def humancheck(self,matrix):
        userinput = input("Write the coordonnate xy ( numbers between 0-2) 01 for example : ")
        if len(userinput)==2 and userinput.isdigit():
            tupleuserinput = self.tupleconversion(userinput)
            if self.matrixcheck(matrix,tupleuserinput): 
                return True,tupleuserinput
        return False,None
        
    def inputcheck(self,matrix):
        while(True):
           userinput = self.humancheck(matrix)
           if userinput[0]: return userinput[1]



            
