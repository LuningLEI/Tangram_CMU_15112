from cmu_graphics import *
import copy, string, itertools, random, math
import random, itertools, string, copy
import tangram as tg

################## Puzzle Theme ##############

# ( Tutor 1 ) #

def getBoardT1():
    puzzle1 = tg.Model_Puzzle(450,280,50,100,0,100,0,0)
    puzzle2 = tg.Model_Puzzle(550,280,0,100,-50,100,0,0)
    puzzle3 = tg.Model_Puzzle(500,200,50,80,0,180,-50,80)
    return [puzzle1,puzzle2, puzzle3]
    
def getPiecesT1():
    puzzle1 = tg.Puzzle(random.randint(200,800),random.randint(200,300),50,100,0,100,0,0)
    puzzle2 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,100,-50,100,0,0)
    puzzle3 = tg.Puzzle(random.randint(200,800),random.randint(200,300),50,80,0,180,-50,80)
    return [puzzle1,puzzle2, puzzle3]

# ( Tutor 2 ) #

def getBoardT2():
    puzzle1 = tg.Model_Puzzle(350,180,300,0,150,150,0,0)
    puzzle2 = tg.Model_Puzzle(650,180,0,150,-75,225,-75,75)
    puzzle3 = tg.Model_Puzzle(575,255,0,150,-75,75,0,0)
    puzzle4 = tg.Model_Puzzle(650,330,0,150,-150,150,0,0)
    puzzle5 = tg.Model_Puzzle(500,330,75,75,0,150,-75,75)
    puzzle6 = tg.Model_Puzzle(425,405,75,75,-75,75,0,0)
    puzzle7 = tg.Model_Puzzle(350,180,150,150,0,300,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]
    
def getPiecesT2():
    puzzle1 = tg.Puzzle(random.randint(200,800),random.randint(200,300),300,0,150,150,0,0)
    puzzle2 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,150,-75,225,-75,75)
    puzzle3 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,150,-75,75,0,0)
    puzzle4 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,150,-150,150,0,0)
    puzzle5 = tg.Puzzle(random.randint(200,800),random.randint(200,300),75,75,0,150,-75,75)
    puzzle6 = tg.Puzzle(random.randint(200,800),random.randint(200,300),75,75,-75,75,0,0)
    puzzle7 = tg.Puzzle(random.randint(200,800),random.randint(200,300),150,150,0,300,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]

# ( Tutor 3 ) #

def getBoardT3():
    puzzle1 = tg.Model_Puzzle(500,200,0,150,-150,150,0,0)
    puzzle2 = tg.Model_Puzzle(500,350,0,150,-150,0,0,0)
    puzzle3 = tg.Model_Puzzle(500,200,75,75,0,75,0,0)
    puzzle4 = tg.Model_Puzzle(575,275,0,75,-75,75,-75,0)
    puzzle5 = tg.Model_Puzzle(575,350,-75,75,-75,0,0,0)
    puzzle6 = tg.Model_Puzzle(575,350,0,75,-75, 150,-75,75)
    puzzle7 = tg.Model_Puzzle(575,275,75,75,0,150,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]
    
def getPiecesT3():
    puzzle1 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,150,-150,150,0,0)
    puzzle2 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,150,-150,0,0,0)
    puzzle3 = tg.Puzzle(random.randint(200,800),random.randint(200,300),75,75,0,75,0,0)
    puzzle4 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,75,-75,75,-75,0)
    puzzle5 = tg.Puzzle(random.randint(200,800),random.randint(200,300),-75,75,-75,0,0,0)
    puzzle6 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,75,-75, 150,-75,75)
    puzzle7 = tg.Puzzle(random.randint(200,800),random.randint(200,300),75,75,0,150,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]
    
# ( Cat ) #

def getPiecesCat():
    puzzle1 = tg.Puzzle(random.randint(200,800),random.randint(200,300),50,50,0,100,0,0)
    puzzle2 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,100,-50,50,0,0)
    puzzle3 = tg.Puzzle(random.randint(200,800),random.randint(200,300),50,50,0,100,-50,50)
    puzzle4 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,140,-70,70,0,0)
    puzzle5 = tg.Puzzle(random.randint(200,800),random.randint(200,300),100,100,0,200,0,0)
    puzzle6 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,140,-140,140,0,0)
    puzzle7 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,60,-70,-10,-70,-70)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]

def getBoardCat():
    puzzle1 = tg.Model_Puzzle(450,150,50,50,0,100,0,0)
    puzzle2 = tg.Model_Puzzle(550,150,0,100,-50,50,0,0)
    puzzle3 = tg.Model_Puzzle(500,200,50,50,0,100,-50,50)
    puzzle4 = tg.Model_Puzzle(500,300,0,140,-70,70,0,0)
    puzzle5 = tg.Model_Puzzle(500,300,100,100,0,200,0,0)
    puzzle6 = tg.Model_Puzzle(600,400,0,140,-140,140,0,0)
    puzzle7 = tg.Model_Puzzle(500,440,0,60,-70,-10,-70,-70)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]

# ( Pigeon ) #

def getBoardPigeon():
    puzzle1 = tg.Model_Puzzle(350,200,150,0,75,75,0,0)
    puzzle2 = tg.Model_Puzzle(500,200,0,150,-75,225,-75,75)
    puzzle3 = tg.Model_Puzzle(500,350,0,212,-212,212,0,0)
    puzzle4 = tg.Model_Puzzle(712,138,0,212,-212,212,0,0)
    puzzle5 = tg.Model_Puzzle(606,350,0,106,-106,106,-106,0)
    puzzle6 = tg.Model_Puzzle(606,456,0,106,-106,0,0,0)
    puzzle7 = tg.Model_Puzzle(756,350,-150,150,-150,-0,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]

def getPiecesPigeon():
    puzzle1 = tg.Puzzle(random.randint(200,800),random.randint(200,300),150,0,75,75,0,0)
    puzzle2 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,150,-75,225,-75,75)
    puzzle3 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,212,-212,212,0,0)
    puzzle4 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,212,-212,212,0,0)
    puzzle5 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,106,-106,106,-106,0)
    puzzle6 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,106,-106,0,0,0)
    puzzle7 = tg.Puzzle(random.randint(200,800),random.randint(200,300),-150,150,-150,-0,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]

# ( Sparrow ) #

def getBoardSparrow():
    puzzle1 = tg.Model_Puzzle(700,130,106,106,0,106,-106,0)
    puzzle2 = tg.Model_Puzzle(625,161,75,75,0,150,-75,75)
    puzzle3 = tg.Model_Puzzle(700,236,0,150,-75,75,0,0)
    puzzle4 = tg.Model_Puzzle(550,236,150,150,0,300,0,0)
    puzzle5 = tg.Model_Puzzle(550,236,0,300,-150,150,0,0)
    puzzle6 = tg.Model_Puzzle(400,386,106,106,-106,106,0,0)
    puzzle7 = tg.Model_Puzzle(506,492,106,106,0,106,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]

def getPiecesSparrow():
    puzzle1 = tg.Puzzle(random.randint(200,800),random.randint(200,300),106,106,0,106,-106,0)
    puzzle2 = tg.Puzzle(random.randint(200,800),random.randint(200,300),75,75,0,150,-75,75)
    puzzle3 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,150,-75,75,0,0)
    puzzle4 = tg.Puzzle(random.randint(200,800),random.randint(200,300),150,150,0,300,0,0)
    puzzle5 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,300,-150,150,0,0)
    puzzle6 = tg.Puzzle(random.randint(200,800),random.randint(200,300),106,106,-106,106,0,0)
    puzzle7 = tg.Puzzle(random.randint(200,800),random.randint(200,300),106,106,0,106,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]

# ( Rabbit ) #
def getBoardRabbit():
    puzzle1 = tg.Model_Puzzle(450,150,70,0,140,70,70,70)
    puzzle2 = tg.Model_Puzzle(620,220,0,70,-70,70,-70,0)
    puzzle3 = tg.Model_Puzzle(550,220,0,140,-140,140,0,0)
    puzzle4 = tg.Model_Puzzle(550,360,-140,140,-140,0,0,0)
    puzzle5 = tg.Model_Puzzle(550,310,50,50,0,100,0,0)
    puzzle6 = tg.Model_Puzzle(510,400,0,100,-100,100,0,0)
    puzzle7 = tg.Model_Puzzle(510,400,50,50,0,100,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]

def getPiecesRabbit():
    puzzle1 = tg.Puzzle(random.randint(200,800),random.randint(200,300),70,0,140,70,70,70)
    puzzle2 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,70,-70,70,-70,0)
    puzzle3 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,140,-140,140,0,0)
    puzzle4 = tg.Puzzle(random.randint(200,800),random.randint(200,300),-140,140,-140,0,0,0)
    puzzle5 = tg.Puzzle(random.randint(200,800),random.randint(200,300),50,50,0,100,0,0)
    puzzle6 = tg.Puzzle(random.randint(200,800),random.randint(200,300),0,100,-100,100,0,0)
    puzzle7 = tg.Puzzle(random.randint(200,800),random.randint(200,300),50,50,0,100,0,0)
    return [puzzle1,puzzle2, puzzle3,puzzle4,puzzle5,puzzle6,puzzle7]