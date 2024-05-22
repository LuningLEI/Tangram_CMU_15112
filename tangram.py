from cmu_graphics import *
import copy, string, itertools, random, math
import random, itertools, string, copy

class Puzzle:
    colorlist = ['plum','mediumPurple','darkSlateBlue','darkGreen','darkRed', 'yellow','pink','lightSeaGreen','cornflowerBlue','orange','cyan']
    puzzle_color = random.choice(colorlist)
    def __init__(self, x1, y1, dx2, dy2, dx3, dy3, dx4, dy4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1+dx2
        self.y2 = y1+dy2
        self.x3 = x1+dx3
        self.y3 = y1+dy3
        self.x4 = x1+dx4
        self.y4 = y1+dy4
        puzzle_color = random.choice(Puzzle.colorlist)
        self.color = puzzle_color
        self.move = False
        self.show = True
    
    def getLines(self):
        line1 = (self.x1, self.y1, self.x2, self.y2)
        line2 = (self.x2, self.y2, self.x3, self.y3)
        line3 = (self.x3, self.y3, self.x4, self.y4)
        line4 = (self.x4, self.y4, self.x1, self.y1)
        return [line1,line2,line3, line4]
        
    def __repr__(self):
        return f'Puzzle with color ={self.color}, move = {self.move}, show = {self.show}'

    def __eq__(self, other):
        if isinstance(other, Puzzle) == True:
            if (self.x1, self.y1) == (other.x1, other.y1) and  (self.x2, self.y2) == (other.x2, other.y2) and  (self.x3, self.y3) == (other.x3, other.y3):
                return True
        return False
    
    def mostlyPlaced_Correct(self,other):
        if isinstance(other, Puzzle) == True:
            if distance(self.x1, self.y1, other.x1, other.y1) <=5 and distance(self.x2, self.y2, other.x2, other.y2) <=5 and distance(self.x3, self.y3, other.x3, other.y3) <=5 and distance(self.x4, self.y4, other.x4, other.y4) <=5:
                return True
        return False
        
    def mostlyPlaced_Wrong(self,other):
        if isinstance(other, Puzzle):
            lines1 = self.getLines()
            lines2 = other.getLines()
            for line1 in lines1:
                for line2 in lines2:
                    self_point1x, self_point1y, self_point2x, self_point2y = line1
                    other_point1x,other_point1y,other_point2x,other_point2y = line2
                    if distance(self_point1x, self_point1y, self_point2x, self_point2y) == distance(other_point1x,other_point1y,other_point2x,other_point2y):
                        if distance(self_point1x,self_point1y,other_point1x,other_point1y) <=5 and distance(self_point2x,self_point2y,other_point2x,other_point2y)<=5:
                            difx = self_point1x-other_point1x
                            dify = self_point1y - other_point1y 
                            return difx, dify
            return None
        
class Model_Puzzle(Puzzle):
    def __init__(self, x1, y1, dx2, dy2, dx3, dy3, dx4, dy4):
        super().__init__(x1, y1, dx2, dy2, dx3, dy3, dx4, dy4)
        self.color = 'lightGray'
        