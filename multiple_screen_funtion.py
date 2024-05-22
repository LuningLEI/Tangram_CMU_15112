from cmu_graphics import *
import copy, string, itertools, random, math
import random, itertools, string, copy

############## Functions Used by Multiple Screens ###############

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def inRect(mouseX,mouseY,x1,y1,dx,dy):
    x2 = x1 + dx
    y2 = y1 + dy
    if x1 <= mouseX <= x2 and y1 <= mouseY <= y2:
        return True
    else:
        return False
        
# Check A Point is in the A Polygon 
def countIntersect(shape,mouseX,mouseY):
    count = 0
    for line in shape:
        x1,y1,x2,y2 = line
        if checkIntersect(x1,y1,x2,y2,mouseX,mouseY) == True:
            count += 1
    return count

def checkIntersect(x1,y1,x2,y2,mouseX,mouseY):
    if x1 != x2 and y1 != y2:
        k = (y2-y1)/(x2-x1)
        b = y1-k*x1
        x = (mouseY-b)/k
        if x1 <= x2:
            if x1 <= x <= x2 and x >= mouseX:
                return True
        else:
            if x2 <= x <= x1 and x >= mouseX:
                return True
    elif x1 == x2:
        if mouseX < x1:
            if y1 <= y2:
                if y1 <= mouseY <= y2:
                    return True
            else:
                if y2 <= mouseY <= y1:
                    return True
    return False

# Drawing (for TutorScreen and PlayScreen):

def drawPuzzleAndBoard(app):
    for puzzle in app.puzzles[::-1]:
            if puzzle.show == True:
                if puzzle == app.selectedPuzzle:
                    drawPolygon(puzzle.x1, puzzle.y1, puzzle.x2, puzzle.y2, puzzle.x3, puzzle.y3, puzzle.x4, puzzle.y4, fill = puzzle.color, border = 'green', borderWidth = 4)
                else:
                    drawPolygon(puzzle.x1, puzzle.y1, puzzle.x2, puzzle.y2, puzzle.x3, puzzle.y3, puzzle.x4, puzzle.y4, fill = puzzle.color)
    for board in app.boards:
        if app.hint == True:
            drawPolygon(board.x1, board.y1, board.x2, board.y2, board.x3, board.y3, board.x4, board.y4, fill = board.color, opacity = 60, border = "black", dashes = True)
        else:
            drawPolygon(board.x1, board.y1, board.x2, board.y2, board.x3, board.y3, board.x4, board.y4, fill = board.color, opacity = 60)

def drawButtons(app):
    drawRect(900,500,80,30, fill = "steelBlue")
    drawLabel("Back",940,515, size = 16)
    drawRect(900,550,80,30, fill = "mediumAquamarine")
    drawLabel("Next",940,565, size = 16)
    
def storeOldValue(app, mouseX, mouseY):
    # store old value of the puzzle (at the start of moving)
    for puzzle in app.puzzles:
        shape = puzzle.getLines()
        if countIntersect(shape,mouseX,mouseY) % 2 == 1:
            puzzle.move = True
            puzzle.show = True
            app.selectedPuzzle = puzzle
            app.startx,app.starty = mouseX,mouseY
            app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 = puzzle.x1,puzzle.y1,puzzle.x2,puzzle.y2,puzzle.x3,puzzle.y3,puzzle.x4,puzzle.y4
            for board in app.boards:
                if puzzle == board:
                    board.color = 'lightGray'
            break
        else:
            puzzle.move = False
            
def movePuzzle(app,mouseX,mouseY):
    app.selectedPuzzle = None
    for puzzle in app.puzzles:
        if puzzle.move == True:
            app.selectedPuzzle = puzzle
            dx,dy = mouseX-app.startx, mouseY-app.starty
            puzzle.x1 = dx + app.x1 
            puzzle.y1 = dy + app.y1
            puzzle.x2 = dx + app.x2
            puzzle.y2 = dy + app.y2
            puzzle.x3 = dx + app.x3
            puzzle.y3 = dy + app.y3
            puzzle.x4 = dx + app.x4
            puzzle.y4 = dy + app.y4
            break
    
def placePuzzle(app,mouseX,mouseY):
    for board in app.boards:
        if board.mostlyPlaced_Correct(app.selectedPuzzle) == True:
            board.color = app.selectedPuzzle.color
            app.selectedPuzzle.show = False
            app.selectedPuzzle.move = False
            app.startx, app.starty = 0,0
            app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 = 0,0,0,0,0,0,0,0
            app.selectedPuzzle.x1 = board.x1
            app.selectedPuzzle.y1 = board.y1
            app.selectedPuzzle.x2 = board.x2
            app.selectedPuzzle.y2 = board.y2
            app.selectedPuzzle.x3 = board.x3
            app.selectedPuzzle.y3 = board.y3
            app.selectedPuzzle.x4 = board.x4
            app.selectedPuzzle.y4 = board.y4
            return
    for board in app.boards:
        if board.mostlyPlaced_Wrong(app.selectedPuzzle) != None:     
            # Even the user placed in the wrong place, the tamgram can go to the line that has the same length
            difx, dify = board.mostlyPlaced_Wrong(app.selectedPuzzle)
            app.selectedPuzzle.x1 += difx
            app.selectedPuzzle.y1 += dify
            app.selectedPuzzle.x2 += difx
            app.selectedPuzzle.y2 += dify
            app.selectedPuzzle.x3 += difx
            app.selectedPuzzle.y3 += dify
            app.selectedPuzzle.x4 += difx
            app.selectedPuzzle.y4 += dify
            app.selectedPuzzle = None
            return

def boardCompletion(app):
    # Check whether the board is completed
        if app.puzzles == []:
            app.finish = False
        else:
            remaining = []
            for puzzle in app.puzzles:
                if puzzle.show == True:
                    remaining.append(puzzle)
            if remaining == []:
                app.finish = True
            else:
                app.finish = False
            
    