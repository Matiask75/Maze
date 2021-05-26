from main_2D import Ascii2D
import random as r

class MazeGen:             

    def generer_lab(self,x,y):
        lab=[[r.choice([" ","|"]) for _ in range(x)] for _ in range(y)]
    return lab

for x in MazeGen.generer_lab(MazeGen,10,10):
    print(*x)

    
