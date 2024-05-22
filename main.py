from cmu_graphics import *
import copy, string, itertools, random, math
import random, itertools, string, copy
import tangram as tg
from multiple_screen_funtion import *
from Theme_setup import *
    
def onAppStart(app):
    # image and sound
    app.welcome_bgp = "cmu://785714/30138167/tangrams_welcome.jpg"
    app.tutor_bgp = "cmu://785714/30138284/tutor_bg.jpg"
    app.getStart_bgp = "cmu://785714/30138704/getStart_bgp.JPG"
    app.catPuzzle = 'cmu://785714/30138971/cat.jpg'
    app.pigeonPuzzle = 'cmu://785714/30138974/pigeon.jpg'
    app.rabbitPuzzle = 'cmu://785714/30138977/rabbit.jpg'
    app.sparrowPuzzle = 'cmu://785714/30138980/sparrow.jpg'
    app.gotit = 'cmu://785714/30140467/fail.jpg'
    app.nop = 'cmu://785714/30140463/gotit.jpg'
    app.sound = Sound('image_and_sound/makabaka.mp3')
    # basic setting
    app.width = 1000
    app.height = 600
    # TutorScreen + PlayScreen
    app.hint = False
    app.puzzles = []
    app.boards = []
    app.finish = False
    app.theme = 'T3'
    changePuzzleTheme(app)
    app.selectedPuzzle = None
    app.labelcolor = 'black'
    app.NextReminder = False
    # GetStartScreen
    app.selectThemeReminder = False
    app.highlightX, app.highlightY = None,None
    # PlayScreen
    app.endOfGame = False
    
############ Welcome Screen #############
 
def WelcomeScreen_redrawAll(app):
    app.sound.play(loop=True)
    imageWidth,imageHeight =getImageSize(app.welcome_bgp)
    drawImage(app.welcome_bgp,0,0,width=imageWidth//3, height=imageHeight//3)

def WelcomeScreen_onMousePress(app,mouseX,mouseY):
    if inRect(mouseX,mouseY,445,355,290,55):
        setActiveScreen('TutorScreen')
        app.theme = "T1"
        changePuzzleTheme(app)
        
############ Tutor Screen ###############

def TutorScreen_redrawAll(app):
    #Basic Settings
    imageWidth,imageHeight =getImageSize(app.tutor_bgp)
    drawImage(app.tutor_bgp,0,0,width=imageWidth//3, height=imageHeight//3)
    drawLabel("Tutorial for beginners", 500,70,size = 25, fill = app.labelcolor)
    drawLabel("Use Mouse to drag tangrams to fill the shadow area:", 50,150,size = 16, align = 'left', fill = app.labelcolor)
    drawLabel("(Press 'h' to get hint)", 50,180,size = 16, align = 'left', fill = app.labelcolor)
    # Buttonss
    drawButtons(app)
    drawRect(40,80,130,20, fill = "lightGray")
    drawLabel("Skip tutorials",105,90, size = 16)
    # Draw the board and puzzles
    drawPuzzleAndBoard(app)
    # Complete
    if app.finish == True:
        if app.theme == "T1":
            drawLabel("You Got It!",app.width//2, app.height-130,size = 16,fill = app.labelcolor)
            drawLabel("Now you know the basic rules of tangrams!",app.width//2, app.height-100,size = 16,fill = app.labelcolor)
            drawLabel("(Tutorial: 1/3)", app.width//2, app.height-70,size = 16,fill = app.labelcolor)
        elif app.theme == "T2":
            drawLabel("You Got It!",app.width//2, app.height-100,size = 16,fill = app.labelcolor)
            drawLabel("(Tutorial: 2/3)", app.width//2, app.height-70,size = 16,fill = app.labelcolor)
        elif app.theme == "T3":
            drawLabel("You passed all tutorials!",app.width//2, app.height-80,size = 16,fill = app.labelcolor)
            drawLabel("Click 'next' to enjoy", app.width//2, app.height-50,size = 16,fill = app.labelcolor)
    if app.NextReminder == True:
        drawLabel("You didn't complete the tangrams!",app.width//2, app.height-80,size = 16,fill = 'red')
        
def TutorScreen_onKeyPress(app,key):
    if key == 'h':
        app.hint = not app.hint

def TutorScreen_onMousePress(app,mouseX,mouseY):
    app.NextReminder = False
    storeOldValue(app, mouseX, mouseY)
    # go Back or Next
    if inRect(mouseX,mouseY,900,500,80,30): # Back
        if app.theme == 'T1':
            setActiveScreen('WelcomeScreen')
        elif app.theme == 'T2':
            app.theme = "T1"
            changePuzzleTheme(app)
        elif app.theme == 'T3':
            app.theme = "T2"
            changePuzzleTheme(app)
    elif inRect(mouseX,mouseY,900,550,80,30): # Next
        if app.finish == True:
            if app.theme == 'T1':
                app.theme = "T2"
                changePuzzleTheme(app)
            elif app.theme == 'T2':
                app.theme = "T3"
                changePuzzleTheme(app)
            elif app.theme == 'T3':
                setActiveScreen('GetStartScreen')
        else:
            app.NextReminder = True
    # Skip tutorials
    if inRect(mouseX,mouseY,40,80,130,20):
        setActiveScreen('GetStartScreen')
    
def TutorScreen_onMouseDrag(app, mouseX, mouseY):
    movePuzzle(app, mouseX, mouseY)

def TutorScreen_onMouseRelease(app, mouseX, mouseY):
    placePuzzle(app,mouseX,mouseY)
    
def TutorScreen_onStep(app):
    boardCompletion(app)

def changePuzzleTheme(app):
    app.finish = False
    app.NextReminder = False
    app.hint = False
    # Change puzzle theme:
    if app.theme == "T1":
        app.puzzles = getPiecesT1()
        app.boards = getBoardT1()
    elif app.theme == "T2":
        app.puzzles = getPiecesT2()
        app.boards = getBoardT2()
    elif app.theme == "T3":
        app.puzzles = getPiecesT3()
        app.boards = getBoardT3()

############ GetStart Screen #############

def GetStartScreen_redrawAll(app):
    imageWidth,imageHeight =getImageSize(app.getStart_bgp)
    drawImage(app.getStart_bgp,0,0,width=imageWidth//3, height=imageHeight//3)
    # theme Pictures
    imageWidth1,imageHeight1 =getImageSize(app.catPuzzle)
    w,h = imageWidth1//10,imageHeight1//10
    drawImage(app.catPuzzle,200,20,width=w, height=h)
    drawImage(app.pigeonPuzzle,470,20,width=w, height=h)
    drawImage(app.sparrowPuzzle,200,310,width=w, height=h)
    drawImage(app.rabbitPuzzle,470,310,width=w, height=h)
    # button
    drawButtons(app)
    if app.selectThemeReminder == True:
        drawLabel("You need to first select a theme.", app.width//2,app.height//2,size = 20, fill= 'red')
    if app.highlightX != None and app.highlightY != None:
        drawRect(app.highlightX,app.highlightY,205,275,fill = None,border = 'yellow',borderWidth = 4)


def GetStartScreen_onMousePress(app,mouseX,mouseY):
    if inRect(mouseX,mouseY,200,20,205,275):
        selectTheme(app,'cat',200,20)
    elif inRect(mouseX,mouseY,470,20,205,275):
        selectTheme(app,'pigeon',470,20)
    elif inRect(mouseX,mouseY,200,310,205,275):
        selectTheme(app,'sparrow',200,310)
    elif inRect(mouseX,mouseY,470,310,205,275):
        selectTheme(app,'rabbit',470,310)
    elif inRect(mouseX,mouseY,900,550,80,30): # confirm
        if app.theme in ['cat','pigeon','sparrow','rabbit']:
            changeTheme(app)
            setActiveScreen('PlayScreen')
            app.selectThemeReminder = False
            app.highlightX,app.highlightY = None,None
        else:
            app.selectThemeReminder = True
    elif inRect(mouseX,mouseY,900,500,80,30): # back
        app.highlightX, app.highlightY = None,None
        setActiveScreen('TutorScreen')
        app.theme = "T1"
        changePuzzleTheme(app)

def selectTheme(app,theme,x,y):
    if app.theme == theme:
            app.highlightX,app.highlightY = None,None
            app.theme = None
    else:
        app.highlightX,app.highlightY = x,y
        app.selectThemeReminder = False
        app.theme = theme

def changeTheme(app):
    app.hint = False
    app.finish = False
    if app.theme == "cat":
        app.puzzles = getPiecesCat()
        app.boards = getBoardCat()
    elif app.theme == 'pigeon':
        app.puzzles = getPiecesPigeon()
        app.boards = getBoardPigeon()
    elif app.theme == 'sparrow':
        app.puzzles = getPiecesSparrow()
        app.boards = getBoardSparrow()
    elif app.theme == 'rabbit':
        app.puzzles = getPiecesRabbit()
        app.boards = getBoardRabbit()
    
############ Play Screen #############
    
def PlayScreen_redrawAll(app):
    #Basic Settings
    imageWidth,imageHeight =getImageSize(app.tutor_bgp)
    drawImage(app.tutor_bgp,0,0,width=imageWidth//3, height=imageHeight//3)
    drawLabel(f"{app.theme.title()}"" Tangrams", 500,50,size = 50, fill = app.labelcolor,font = 'cursive')
    # Buttonss
    drawRect(900,500,80,30, fill = "steelBlue")
    drawLabel("Back",940,515, size = 16)
    drawRect(900,550,80,30, fill = "mediumAquamarine")
    drawLabel("Next",940,565, size = 16)
    # Draw the board and puzzles
    drawPuzzleAndBoard(app)
    # Complete
    if app.finish == True:
        if app.endOfGame == True:
            drawLabel("This is the last tangrams~",app.width//2, app.height-50,size = 30 ,fill = app.labelcolor)
        else:
            imageWidth,imageHeight =getImageSize(app.gotit)
            drawImage(app.gotit,100,150,width=imageWidth//7, height=imageHeight//7)
            drawLabel("You Got It",252, 280, size = 30,fill = app.labelcolor,rotateAngle = -45)
    if app.NextReminder == True:
        imageWidth,imageHeight =getImageSize(app.nop)
        drawImage(app.nop,100,150,width=imageWidth//7, height=imageHeight//7)
        drawLabel("You didn't complete the tangrams!",180, 350, size = 20,fill = 'red')

def PlayScreen_onMousePress(app,mouseX,mouseY):
    app.NextReminder = False
    storeOldValue(app, mouseX, mouseY)
    # go Back or Next
    if inRect(mouseX,mouseY,900,500,80,30): # Back
        app.endOfGame = False
        setActiveScreen('GetStartScreen')
        app.theme = None
        app.highlightX, app.highlightY = None, None
    elif inRect(mouseX,mouseY,900,550,80,30): # Next
        if app.finish == True:
            if app.theme == 'cat':
                app.theme = "pigeon"
                changeTheme(app)
            elif app.theme == 'pigeon':
                app.theme = "sparrow"
                changeTheme(app)
            elif app.theme == 'sparrow':
                app.theme = "rabbit"
                changeTheme(app)
            elif app.theme == 'rabbit':
                app.endOfGame = True
        else:
            app.NextReminder = True

def PlayScreen_onMouseDrag(app, mouseX, mouseY):
    movePuzzle(app, mouseX, mouseY)

def PlayScreen_onMouseRelease(app, mouseX, mouseY):
    placePuzzle(app,mouseX,mouseY)
    
def PlayScreen_onStep(app):
    boardCompletion(app)

def PlayScreen_onKeyPress(app, key):
    if key == 'h':
        app.hint = not app.hint

    
def main():
    runAppWithScreens(initialScreen='WelcomeScreen')

main()