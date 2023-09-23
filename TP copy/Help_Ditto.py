# Name: Yuna Shin
# Andrew ID: yoonahs

# from typing_extensions import TypeVarTuple
from cmu_112_graphics import *

import random, copy

def appStarted(app): 
    app.allTheSets = list()
    app.newSet = set()
    app.mode = 'mainTitleMode'
    app.removedWalls = set()
    (app.width, app.height) = 693, 672
    (app.rows, app.cols) = 31, 31
    app.listOfWalls = []
    for row in range(app.rows):
        for col in range(app.cols):
            if (row % 2 == 1 and col % 2 == 0) or (row % 2 == 0 and col % 2 == 1):
                app.listOfWalls.append((row, col))
    app.listOfDefaultWalls = []
    for row in range(app.rows):
        for col in range(app.cols):
            if (row % 2 == 1 and col % 2 == 1):
                app.listOfDefaultWalls.append((row, col))
    app.finalAllTheSets = list()
    app.initial = False
    app.mazeGameOver = False
    app.count = 0
    app.countIntoSec = None
    app.gameOver = False
    app.gameOverWin = False
    app.attackDone = False
    app.attackByHWDone = False
    app.myPokemonBack = None
    app.battleState = False
    app.attack1 = None
    app.attack2 = None
    app.attack3 = None
    app.attack4 = None
    app.attack = None
    app.myHP = 100
    app.opponentHP = 100
    #image from https://www.sparkfun.com/products/12002
    app.eceHW = app.loadImage('eceHW.gif')
    app.eceHW2 = app.scaleImage(app.eceHW, 1/3.5)
    app.eceHW3 = ImageTk.PhotoImage(app.eceHW2)
    #image from
    # https://www.walmart.com/ip/Spinning-Prize-Wheel-12-Color-Face-Dry-Erase-Spin-Wheel-with-Classic-Peg-Design/435603611
    app.physicsHW = app.loadImage('physicsHW.gif')
    app.physicsHW2 = app.scaleImage(app.physicsHW, 1/3.5)
    app.physicsHW3 = ImageTk.PhotoImage(app.physicsHW2)
    app.opponentPokemon = None
    app.opponentPokemon2 = None
    app.opponentPokeName = None
    app.opponentName = None
    app.myName = None
    #titleScreen and assignScreen images from https://wallpaperaccess.com/ditto
    #citation: from animation part 4 (loading and scaling images)
    app.titleScreenImage = app.loadImage('titleImage.jpeg')
    app.titleScreenImage2 = app.scaleImage(app.titleScreenImage, 0.8)
    app.assignScreenImage = app.loadImage('assignmentImage.jpeg')
    app.assignScreenImage2 = app.scaleImage(app.assignScreenImage, 0.95)
    #icon, back, tile, barrier, pokemons, background, bases, message images from:
    #https://luka-sj.com/res/PE19 (pokemon essentials)
    app.pikachuIconImage = app.loadImage('PIKACHUicon.png')
    app.pikachuIconImage2 = app.scaleImage(app.pikachuIconImage, 1/1.5)
    app.pikachuIconImage3 = ImageTk.PhotoImage(app.pikachuIconImage2)
    app.blastoiseIconImage = app.loadImage('BLASTOISEicon.png')
    app.blastoiseIconImage2 = app.scaleImage(app.blastoiseIconImage, 1/1.5)
    app.blastoiseIconImage3 = ImageTk.PhotoImage(app.blastoiseIconImage2)
    app.eeveeIconImage = app.loadImage('EEVEEicon.png')
    app.eeveeIconImage2 = app.scaleImage(app.eeveeIconImage, 1/1.5)
    app.eeveeIconImage3 = ImageTk.PhotoImage(app.eeveeIconImage2)
    app.lucarioIconImage = app.loadImage('LUCARIOicon.png')
    app.lucarioIconImage2 = app.scaleImage(app.lucarioIconImage, 1/1.5)
    app.lucarioIconImage3 = ImageTk.PhotoImage(app.lucarioIconImage2)
    app.magikarpIconImage = app.loadImage('MAGIKARPicon.png')
    app.magikarpIconImage2 = app.scaleImage(app.magikarpIconImage, 1/1.5)
    app.magikarpIconImage3 = ImageTk.PhotoImage(app.magikarpIconImage2)
    app.dittoIconImage = app.loadImage('DITTOicon.png')
    app.dittoIconImage2 = app.scaleImage(app.dittoIconImage, 1/1.5)
    app.dittoIconImage3 = ImageTk.PhotoImage(app.dittoIconImage2)
    app.pikachuBackImage = app.loadImage('PIKACHUback.gif')
    app.pikachuBackImage2 = app.scaleImage(app.pikachuBackImage, 1/1.5)
    app.blastoiseBackImage = app.loadImage('BLASTOISEback.gif')
    app.blastoiseBackImage2 = app.scaleImage(app.blastoiseBackImage, 1/1.5)
    app.eeveeBackImage = app.loadImage('EEVEEback.gif')
    app.eeveeBackImage2 = app.scaleImage(app.eeveeBackImage, 1/1.5)
    app.lucarioBackImage = app.loadImage('LUCARIOback.gif')
    app.lucarioBackImage2 = app.scaleImage(app.lucarioBackImage, 1/1.5)
    app.magikarpBackImage = app.loadImage('MAGIKARPback.gif')
    app.magikarpBackImage2 = app.scaleImage(app.magikarpBackImage, 1/1.5)
    app.tileImage = app.loadImage('entireFloor.gif') 
    app.tileImage3 = ImageTk.PhotoImage(app.tileImage)
    app.barrierImage = app.loadImage('wall.gif')
    app.barrierImage2 = app.scaleImage(app.barrierImage, 1/1.4)
    app.barrierImage3 = ImageTk.PhotoImage(app.barrierImage2)
    app.dittoImage = app.loadImage('DITTO.gif')
    app.dittoImage2 = app.scaleImage(app.dittoImage, 1/3.5)
    app.dittoImage3 = ImageTk.PhotoImage(app.dittoImage2)
    app.followingPokemon = app.dittoIconImage2
    app.pikachuImage = app.loadImage('PIKACHU.gif')
    app.pikachuImage2 = app.scaleImage(app.pikachuImage, 1/5)
    app.pikachuImage3 = ImageTk.PhotoImage(app.pikachuImage2)
    app.blastoiseImage = app.loadImage('BLASTOISE.gif')
    app.blastoiseImage2 = app.scaleImage(app.blastoiseImage, 1/8)
    app.blastoiseImage3 = ImageTk.PhotoImage(app.blastoiseImage2)
    app.eeveeImage = app.loadImage('EEVEE.gif')
    app.eeveeImage2 = app.scaleImage(app.eeveeImage, 1/5)
    app.eeveeImage3 = ImageTk.PhotoImage(app.eeveeImage2)
    app.lucarioImage = app.loadImage('LUCARIO.gif')
    app.lucarioImage2 = app.scaleImage(app.lucarioImage, 1/6)
    app.lucarioImage3 = ImageTk.PhotoImage(app.lucarioImage2)
    app.magikarpImage = app.loadImage('MAGIKARP.gif')
    app.magikarpImage2 = app.scaleImage(app.magikarpImage, 1/5)
    app.magikarpImage3 = ImageTk.PhotoImage(app.magikarpImage2)
    app.backgroundImage = app.loadImage('rocky_bg.gif')
    app.backgroundImage2 = app.scaleImage(app.backgroundImage, 2.5)
    app.baseAImage = app.loadImage('rocky_baseA.gif')
    app.baseAImage2 = app.scaleImage(app.baseAImage, 1/2)
    app.baseBImage = app.loadImage('rocky_baseB.gif')
    app.baseBImage2 = app.scaleImage(app.baseBImage, 1/2)
    app.messageImage = app.loadImage('rocky_message.gif')
    app.messageImage2 = app.scaleImage(app.messageImage, 1.4)
    app.dittoBackImage = app.loadImage('DITTOback.gif')
    app.dittoBackImage2 = app.scaleImage(app.dittoBackImage, 1/1.5)
    app.pRow, app.pCol = None, None
    app.bRow, app.bCol = None, None
    app.eRow, app.eCol = None, None
    app.lRow, app.lCol = None, None
    app.mRow, app.mCol = None, None
    app.direction = None
    app.girlRow = 0
    app.girlCol = 0
    spritestripD = app.loadImage('girlDown.gif') #citation: animation part 4
    app.spritesD = []
    for i in range(4):
        sprite = spritestripD.crop((32*i, 0, 32+32*i, 48))
        app.spritesD.append(sprite)
    app.spriteCounterD = 0
    spritestripU = app.loadImage('girlUp.gif') #citation: animation part 4
    app.spritesU = []
    for i in range(4):
        sprite = spritestripU.crop((32*i, 0, 32+32*i, 48))
        app.spritesU.append(sprite)
    app.spriteCounterU = 0
    spritestripL = app.loadImage('girlLeft.gif') #citation: animation part 4
    app.spritesL = []
    for i in range(4):
        sprite = spritestripL.crop((32*i, 0, 32+32*i, 48))
        app.spritesL.append(sprite)
    app.spriteCounterL = 0
    spritestripR = app.loadImage('girlRight.gif') #citation: animation part 4
    app.spritesR = []
    for i in range(4):
        sprite = spritestripR.crop((32*i, 0, 32+32*i, 48))
        app.spritesR.append(sprite)
    app.spriteCounterR = 0
    formMazePattern(app)
    assignPokemonRandomly(app)
    dittoBattleOpponent(app)
    attackChoices(app)
    if app.count == 30:
        app.mazeGameOver = True
    moveOnToNextMode(app)

###############################################################################

###### Main Title Mode ######

# from animation part 4 (modes)
def mainTitleMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2,
                        image = ImageTk.PhotoImage(app.titleScreenImage2))
    canvas.create_text(app.width/2, 120, text='HELP, DITTO!', 
                        font='Arial 30 bold',
                        fill='black')
    canvas.create_text(app.width/2, 170, 
                        text='15-112 Term Project by Yuna Shin',
                       font='Arial 20 bold')
    canvas.create_text(app.width/2, 500, 
                        text='Press any key to start transforming your ditto!',
                       font='Arial 15', fill='black')

def mainTitleMode_keyPressed(app, event):
    app.mode = 'mazeMode'

###############################################################################

###### Maze Mode ######

def mazeMode_timerFired(app):
    app.spriteCounterD = (1 + app.spriteCounterD) % len(app.spritesD)
    app.spriteCounterU = (1 + app.spriteCounterU) % len(app.spritesU)
    app.spriteCounterL = (1 + app.spriteCounterL) % len(app.spritesL)
    app.spriteCounterR = (1 + app.spriteCounterR) % len(app.spritesR)
    if app.initial == False:
        formMazePattern(app)
        dittoBattleOpponent(app)
    app.timerDelay = 10
    app.count += 1
    app.countIntoSec = str(30 - app.count//10)
    if app.count == 300:
        app.mazeGameOver = True

def drawMazeGameOver(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
            text='GAME OVER! Try again by pressing "r".', 
            font='Arial 30 bold', fill='yellow')

def drawMazeGameOver2(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
            text='TIME OVER! Press any key to move on.', 
            font='Arial 30 bold', fill='yellow')

def moveOnToNextMode(app):
    if app.mazeGameOver and app.followingPokemon != app.dittoIconImage2:
        app.mode = 'cmuMode'
    
def drawTimer(app, canvas):
    canvas.create_text(app.width/2, app.height/20,
    text='Remaining Time:', font='Arial 15 bold', fill='yellow')
    canvas.create_text(app.width/2, app.height/10,
    text=app.countIntoSec, font='Arial 15 bold', fill='yellow')

def drawTile(app, canvas):
    canvas.create_image(app.width/20, app.height/20,
                        image = app.tileImage3)

def drawWall(app, canvas, row, col):
    (x0, y0, x1, y1) = getCellBounds(app, row, col)
    canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0, 
                        image = app.barrierImage3)

def getCellBounds(app, row, col):
    x0 = app.width * col / app.cols
    x1 = app.width * (col+1) / app.cols
    y0 = app.height * row / app.rows
    y1 = app.height * (row+1) / app.rows
    return (x0, y0, x1, y1)

def drawMap(app, canvas):
    drawTile(app, canvas)
    drawDefaultWalls(app, canvas)
    drawWalls(app, canvas)
    if app.mazeGameOver == False:
        drawTimer(app, canvas)
    if app.mazeGameOver == True and app.followingPokemon == app.dittoIconImage2:
        drawMazeGameOver(app, canvas)
    if app.mazeGameOver == True and app.followingPokemon != app.dittoIconImage2:
        drawMazeGameOver2(app, canvas)

def drawDefaultWalls(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            if row % 2 == 1 and col % 2 == 1:
                drawWall(app, canvas, row, col)

def drawWalls(app, canvas):
    for index in range(len(app.listOfWalls)):
        row, col = app.listOfWalls[index]
        drawWall(app, canvas, row, col)

#citation: got an idea from:
#Kruskal's algorithm from 112 maze gen pdf 
#https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Kruskal's_algorithm
def createSet(app):
    for row in range(app.rows):
        for col in range(app.cols):
            if (row % 2 == 0 and col % 2 == 0):
                app.allTheSets.append(set([(row, col)]))

def addTogether(app, randomI, randomJ, randomI2, randomJ2, i, j):
    set1 = None
    set2 = None
    for eachSet in app.allTheSets:
        if tuple((randomI, randomJ)) in eachSet:
            set1 = eachSet
    for eachSet2 in app.allTheSets:
        if tuple((randomI2, randomJ2)) in eachSet2:
            set2 = eachSet2
    addTogether2(app, set1, set2, i, j)

def addTogether2(app, set1, set2, wallI, wallJ):
    if (set1 != set2 and set1 != None and set2 != None):
        app.allTheSets.remove(set1)
        app.allTheSets.remove(set2)
        listOfSet1 = list(set1)
        listOfSet2 = list(set2)
        listOfWall = [(wallI, wallJ)]
        app.newSet = set(listOfSet1 + listOfSet2 + listOfWall)
        app.allTheSets.append(app.newSet)
        app.listOfWalls.remove(tuple((wallI, wallJ)))
        app.removedWalls.add(tuple((wallI, wallJ)))
            
def formMazePattern(app):
    createSet(app)
    copyOfListOfWalls = copy.deepcopy(app.listOfWalls)
    random.shuffle(copyOfListOfWalls)
    for (randomI, randomJ) in copyOfListOfWalls:
        leftI, leftJ = randomI, randomJ-1
        rightI, rightJ = randomI, randomJ+1
        upI, upJ = randomI-1, randomJ
        downI, downJ = randomI+1, randomJ
        if len(app.removedWalls) >= 255:
            break
        if ((leftI, leftJ) not in app.listOfWalls and
            (rightI, rightJ) not in app.listOfWalls and
            (leftI, leftJ) not in app.listOfDefaultWalls and
            (rightI, rightJ) not in app.listOfDefaultWalls):
            addTogether(app, leftI, leftJ, rightI, rightJ, randomI, randomJ)
        if ((upI, upJ) not in app.listOfWalls and
            (downI, downJ) not in app.listOfWalls and
            (upI, upJ) not in app.listOfDefaultWalls and
            (downI, downJ) not in app.listOfDefaultWalls):
            addTogether(app, upI, upJ, downI, downJ, randomI, randomJ)
    app.finalAllTheSets = app.allTheSets


def mazeMode_keyPressed(app, event):
    if not app.mazeGameOver:
        drow, dcol = 0, 0 
        if event.key == "h":
            app.mode = 'helpMode'
        if event.key == "b":
            app.mode = 'dittoBattleMode'
        if event.key == "Up":
            drow, dcol = -1, 0
            app.direction = "Up"
        elif event.key == "Down":
            drow, dcol = +1, 0
            app.direction = "Down"
        elif event.key == "Left":
            drow, dcol = 0, -1
            app.direction = "Left"
        elif event.key == "Right":
            drow, dcol = 0, +1
            app.direction = "Right"
        elif event.key == "n":
            app.mode = 'cmuMode'
        elif event.key == "r":
            appStarted(app)
        moveGirl(app, drow, dcol)
    if app.mazeGameOver and app.followingPokemon == app.dittoIconImage2:
        if event.key == "r":
            appStarted(app)
    if app.mazeGameOver and app.followingPokemon != app.dittoIconImage2:
        app.mode = 'cmuMode'

def moveGirl(app, drow, dcol):
    app.girlRow += drow
    app.girlCol += dcol
    if not movementIsLegal(app):
        app.girlRow -= drow
        app.girlCol -= dcol
        return False
    else:
        return True

def movementIsLegal(app):
    if ((app.girlRow, app.girlCol) in app.listOfWalls or
        (app.girlRow, app.girlCol) in app.listOfDefaultWalls or
        app.girlRow < 0 or app.girlCol < 0):
        return False
    else:
        return True

def drawGirl(app, canvas):
    (x0, y0, x1, y1) = getCellBounds(app, app.girlRow, app.girlCol)
    if app.direction == "Up":
        sprite = app.spritesU[app.spriteCounterU]
        canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                            image=ImageTk.PhotoImage(sprite))
    elif app.direction == "Down" or app.direction == None:
        sprite = app.spritesD[app.spriteCounterD]
        canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                            image=ImageTk.PhotoImage(sprite))
    elif app.direction == "Left":
        sprite = app.spritesL[app.spriteCounterL]
        canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                            image=ImageTk.PhotoImage(sprite))
    elif app.direction == "Right":
        sprite = app.spritesR[app.spriteCounterR]
        canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                            image=ImageTk.PhotoImage(sprite))

def assignPokemonRandomly(app):
    copyOfFinalAllTheSets = copy.copy(app.finalAllTheSets[0])
    copyOfFinalAllTheSets = list(copyOfFinalAllTheSets)
    random.shuffle(copyOfFinalAllTheSets)
    app.pRow, app.pCol = copyOfFinalAllTheSets[0]
    app.bRow, app.bCol = copyOfFinalAllTheSets[1]
    app.eRow, app.eCol = copyOfFinalAllTheSets[2]
    app.lRow, app.lCol = copyOfFinalAllTheSets[3]
    app.mRow, app.mCol = copyOfFinalAllTheSets[4]

def drawPokemonRandomly(app, canvas):
    (x0, y0, x1, y1) = getCellBounds(app, app.pRow, app.pCol)
    canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                        image=app.pikachuImage3)
    (x0, y0, x1, y1) = getCellBounds(app, app.bRow, app.bCol)
    canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                        image=app.blastoiseImage3)
    (x0, y0, x1, y1) = getCellBounds(app, app.eRow, app.eCol)
    canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                        image=app.eeveeImage3)
    (x0, y0, x1, y1) = getCellBounds(app, app.lRow, app.lCol)
    canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                        image=app.lucarioImage3)
    (x0, y0, x1, y1) = getCellBounds(app, app.mRow, app.mCol)
    canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                        image=app.magikarpImage3)

def drawFollowingPokemon(app, canvas):
    if app.direction == "Up":
        (x0, y0, x1, y1) = getCellBounds(app, app.girlRow+1, app.girlCol)
        canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0, 
                            image=ImageTk.PhotoImage(app.followingPokemon))
    elif app.direction == "Down":
        (x0, y0, x1, y1) = getCellBounds(app, app.girlRow-1, app.girlCol)
        canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                            image=ImageTk.PhotoImage(app.followingPokemon))
    elif app.direction == "Left":
        (x0, y0, x1, y1) = getCellBounds(app, app.girlRow, app.girlCol+1)
        canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                            image=ImageTk.PhotoImage(app.followingPokemon))
    elif app.direction == "Right":
        (x0, y0, x1, y1) = getCellBounds(app, app.girlRow, app.girlCol-1)
        canvas.create_image((x1-x0)/2 + x0, (y1-y0)/2 + y0,
                            image=ImageTk.PhotoImage(app.followingPokemon))

###############################################################################

###### Ditto Battle Mode ######

def drawDitto(app, canvas):
    canvas.create_image(1*app.width/4, 2.15*app.height/3,
                        image=ImageTk.PhotoImage(app.dittoBackImage2))

def drawBattleOpponent(app, canvas):
    canvas.create_image(3*app.width/4, 0.8*app.height/3,
                        image=ImageTk.PhotoImage(app.opponentPokemon))

def drawChoicesDitto(app, canvas):
    canvas.create_rectangle(0, app.height/3, app.width/5, 1.3*app.height/3,
                        fill='lightGrey', outline='black', width=1)
    canvas.create_rectangle(app.width/5, app.height/3, 2*app.width/5,
                    1.3*app.height/3, fill='lightGrey', outline='black',
                        width=1)
    canvas.create_rectangle(0, 1.3*app.height/3, app.width/5, 1.6*app.height/3,
                        fill='lightGrey', outline='black', width=1)
    canvas.create_rectangle(app.width/5, 1.3*app.height/3, 2*app.width/5,
                    1.6*app.height/3, fill='lightGrey', outline='black', width=1)
    canvas.create_text(0.4*app.width/5, 1.15*app.height/3, text='(1) Transform')

def dittoBattleOpponent(app):
    if (app.girlRow, app.girlCol) == (app.pRow, app.pCol):
        app.opponentPokeName = 'Pikachu'
        app.opponentPokemon = app.pikachuImage
        app.opponentPokemon2 = app.pikachuImage3
    elif (app.girlRow, app.girlCol) == (app.bRow, app.bCol):
        app.opponentPokeName = 'Blastoise'
        app.opponentPokemon = app.blastoiseImage
        app.opponentPokemon2 = app.blastoiseImage3
    elif (app.girlRow, app.girlCol) == (app.eRow, app.eCol):
        app.opponentPokeName = 'Eevee'
        app.opponentPokemon = app.eeveeImage
        app.opponentPokemon2 = app.eeveeImage3
    elif (app.girlRow, app.girlCol) == (app.lRow, app.lCol):
        app.opponentPokeName = 'Lucario'
        app.opponentPokemon = app.lucarioImage
        app.opponentPokemon2 = app.lucarioImage3
    elif (app.girlRow, app.girlCol) == (app.mRow, app.mCol):
        app.opponentPokeName = 'Magikarp'
        app.opponentPokemon = app.magikarpImage
        app.opponentPokemon2 = app.magikarpImage3

def dittoBattleMode_keyPressed(app, event):
    if event.key == '1' and app.opponentPokemon == app.pikachuImage:
        app.followingPokemon = app.pikachuIconImage2
        app.myPokemonBack = app.pikachuBackImage2
        app.myName = 'Pikachu'
        app.mode = 'mazeMode'
    if event.key == '1' and app.opponentPokemon == app.blastoiseImage:
        app.followingPokemon = app.blastoiseIconImage2
        app.myPokemonBack = app.blastoiseBackImage2
        app.myName = 'Blastoise'
        app.mode = 'mazeMode'
    if event.key == '1' and app.opponentPokemon == app.eeveeImage:
        app.followingPokemon = app.eeveeIconImage2
        app.myPokemonBack = app.eeveeBackImage2
        app.myName = 'Eevee'
        app.mode = 'mazeMode'
    if event.key == '1' and app.opponentPokemon == app.magikarpImage:
        app.followingPokemon = app.magikarpIconImage2
        app.myPokemonBack = app.magikarpBackImage2
        app.myName = 'Magikarp'
        app.mode = 'mazeMode'
    if event.key == '1' and app.opponentPokemon == app.lucarioImage:
        app.followingPokemon = app.lucarioIconImage2
        app.myPokemonBack = app.lucarioBackImage2
        app.myName = 'Lucario'
        app.mode = 'mazeMode'
    elif event.key == '5':
        app.mode = 'mazeMode'

def dittoBattleMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.backgroundImage2))
    canvas.create_image(3*app.width/4, app.height/3,
                        image=ImageTk.PhotoImage(app.baseBImage))
    canvas.create_image(1*app.width/4, 3*app.height/4,
                        image=ImageTk.PhotoImage(app.baseAImage2))
    drawChoicesDitto(app, canvas)
    drawBattleOpponent(app, canvas)
    drawDitto(app, canvas)
    drawHPBoxes(app, canvas)
    canvas.create_text(3.15*app.width/4, 2.05*app.height/3,
    text='Ditto', fill='black', font='Arial 12 bold')
    canvas.create_text(1.65*app.width/4, 0.55*app.height/3,
    text=app.opponentPokeName, fill='black', font='Arial 12 bold')
    canvas.create_image(app.width/2, 7*app.height/8,
                        image=ImageTk.PhotoImage(app.messageImage2))
    canvas.create_text(app.width/2, 7*app.height/8,
    text='Press "5" to run away.')

def mazeMode_redrawAll(app, canvas):
    drawMap(app, canvas)
    drawPokemonRandomly(app, canvas)
    drawFollowingPokemon(app, canvas)
    drawGirl(app, canvas)

###############################################################################

###### Maze Help Mode ######

def helpMode_redrawAll(app, canvas):
    font = 'Arial 13'
    canvas.create_text(app.width/2, 150, 
                    text='Help', 
                       font='Arial 20 bold', fill='black')
    canvas.create_text(app.width/2, 250, 
    text='Transform your ditto into another pokemon by starting a battle!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 275,
    text="If you don't like the pokemon you just encountered, run away",
                        font=font, fill='black')
    canvas.create_text(app.width/2, 300,
    text='After transforming your ditto, press "n" to move to CMU',
                        font=font, fill='black')
    canvas.create_text(app.width/2, 325,
    text="If you don't transform your ditto until the time is over, you lose.",
                        font=font, fill='black')
    canvas.create_text(app.width/2, 350, 
    text='When the time is over, you are forced to move to CMU with your pokemon.',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 375,
                    text='Press any key to return to the game!',
                       font=font, fill='black')

def helpMode_keyPressed(app, event):
    app.mode = 'mazeMode'

###############################################################################

###### CMU Mode ######

def cmuMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.assignScreenImage2))
    drawCMU(app, canvas)

def cmuMode_keyPressed(app, event):
    if event.key == "h":
        app.mode = 'cmuHelpMode'
    elif event.key == "1":
        app.opponentPokemon = app.eceHW2
        app.opponentName = 'Breadboard'
        app.mode = 'cmuBattleMode'
        attackChoices(app)
    elif event.key == "2":
        app.opponentPokemon = app.physicsHW2
        app.mode = 'cmuBattleMode'
        app.opponentName = 'Spinning Wheel'
        attackChoices(app)

def drawCMU(app, canvas):
    font = 'Arial 15'
    canvas.create_text(app.width/2, 150, 
                    text='~LIST OF ASSIGNMENTS~', 
                       font='Arial 20 bold', fill='black')
    canvas.create_text(app.width/2, 250, 
    text='Press the number of assignment you want to begin!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 300,
    text='1: 18100 Intro to ECE homework', font=font, fill='black')
    canvas.create_text(app.width/2, 330,
    text='(Connect the wires to make a circuit!)', font=font, fill='black')
    canvas.create_text(app.width/2, 370,
    text='2: 33141 Physics1 homework', font=font, fill='black')
    canvas.create_text(app.width/2, 400,
    text='(Measure the velocity of a spinning wheel!)', font=font, fill='black')

###############################################################################

###### CMU Battle Mode ######

def drawChoices(app, canvas):
    canvas.create_rectangle(0, app.height/3, app.width/5, 1.3*app.height/3,
                        fill='lightGrey', outline='black', width=1)
    canvas.create_rectangle(app.width/5, app.height/3, 2*app.width/5,
                    1.3*app.height/3, fill='lightGrey', outline='black',
                        width=1)
    canvas.create_rectangle(0, 1.3*app.height/3, app.width/5, 1.6*app.height/3,
                        fill='lightGrey', outline='black', width=1)
    canvas.create_rectangle(app.width/5, 1.3*app.height/3, 2*app.width/5,
                    1.6*app.height/3, fill='lightGrey', outline='black', width=1)
    canvas.create_text(0.4*app.width/5, 1.15*app.height/3, text=app.attack1,
                    fill='black')
    canvas.create_text(1.5*app.width/5, 1.15*app.height/3, text=app.attack2,
                    fill='black')
    canvas.create_text(0.4*app.width/5, 1.45*app.height/3, text=app.attack3,
                    fill='black')
    canvas.create_text(1.5*app.width/5, 1.45*app.height/3, text=app.attack4,
                    fill='black')

def attackChoices(app): # in the order of ECE hw, Physics1 hw
    if app.myPokemonBack == app.pikachuBackImage2:
        app.attack1 = '(1) Spark' #30, 30
        app.attack2 = '(2) Iron Tail' #10, 30
        app.attack3 = '(3) Thunder' #50, 30
        app.attack4 = '(4) Quick Attack' #10, 10
    elif app.myPokemonBack == app.blastoiseBackImage2:
        app.attack1 = '(1) Bite' #40, 30
        app.attack2 = '(2) Skull Bash' #60, 30
        app.attack3 = '(3) Aqua Tail' #0, 20
        app.attack4 = '(4) Hydro Pump' #0, 20
    elif app.myPokemonBack == app.eeveeBackImage2:
        app.attack1 = '(1) Helping Hand' #40, 40
        app.attack2 = '(2) Copycat' #10, 10
        app.attack3 = '(3) Take Down' #10, 10
        app.attack4 = '(4) Bite' #40, 40
    elif app.myPokemonBack == app.lucarioBackImage2:
        app.attack1 = '(1) Extreme Speed' #20, 40
        app.attack2 = '(2) Close Combat' #30, 20
        app.attack3 = '(3) Dragon Pulse' #20, 20
        app.attack4 = '(4) Metal Claw' #30, 20
    elif app.myPokemonBack == app.magikarpBackImage2:
        app.attack1 = '(1) Splash' #0, 50
        app.attack2 = ''
        app.attack3 = ''
        app.attack4 = ''

def cmuBattleMode_keyPressed(app, event):
    if event.key == "1":
        if (app.myName == 'Pikachu' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 30
            app.attack = 'Spark'
        if (app.myName == 'Pikachu' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 30
            app.attack = 'Spark'
        if (app.myName == 'Blastoise' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 40
            app.attack = 'Bite'
        if (app.myName == 'Blastoise' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 30
            app.attack = 'Bite'
        if (app.myName == 'Eevee' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 40
            app.attack = 'Helping Hand'
        if (app.myName == 'Eevee' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 40
            app.attack = 'Helping Hand'
        if (app.myName == 'Lucario' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 20
            app.attack = 'Extreme Speed'
        if (app.myName == 'Lucario' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 40
            app.attack = 'Extreme Speed'
        if (app.myName == 'Magikarp' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 0
            app.attack = 'Splash'
        if (app.myName == 'Magikarp' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 50
            app.attack = 'Splash'
    if event.key == "2":
        if (app.myName == 'Pikachu' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 10
            app.attack = 'Iron Tail'
        if (app.myName == 'Pikachu' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 30
            app.attack = 'Iron Tail'
        if (app.myName == 'Blastoise' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 60
            app.attack = 'Skull Bash'
        if (app.myName == 'Blastoise' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 30
            app.attack = 'Skull Bash'
        if (app.myName == 'Eevee' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 10
            app.attack = 'Copycat'
        if (app.myName == 'Eevee' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 10
            app.attack = 'Copycat'
        if (app.myName == 'Lucario' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 30
            app.attack = 'Close Combat'
        if (app.myName == 'Lucario' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 20
            app.attack = 'Close Combat'
    if event.key == "3":
        if (app.myName == 'Pikachu' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 50
            app.attack = 'Thunder'
        if (app.myName == 'Pikachu' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 30
            app.attack = 'Thunder'
        if (app.myName == 'Blastoise' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 0
            app.attack = 'Aqua Tail'
        if (app.myName == 'Blastoise' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 20
            app.attack = 'Aqua Tail'
        if (app.myName == 'Eevee' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 10
            app.attack = 'Take Down'
        if (app.myName == 'Eevee' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 10
            app.attack = 'Take Down'
        if (app.myName == 'Lucario' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 20
            app.attack = 'Dragon Pulse'
        if (app.myName == 'Lucario' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 20
            app.attack = 'Dragon Pulse'
    if event.key == "4":
        if (app.myName == 'Pikachu' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 10
            app.attack = 'Quick Attack'
        if (app.myName == 'Pikachu' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 10
            app.attack = 'Quick Attack'
        if (app.myName == 'Blastoise' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 0
            app.attack = 'Hydro Pump'
        if (app.myName == 'Blastoise' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 20
            app.attack = 'Hydro Pump'
        if (app.myName == 'Eevee' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 40
            app.attack = 'Bite'
        if (app.myName == 'Eevee' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 40
            app.attack = 'Bite'
        if (app.myName == 'Lucario' and 
        app.opponentName == 'Breadboard'):
            app.opponentHP -= 30
            app.attack = 'Metal Claw'
        if (app.myName == 'Lucario' and 
        app.opponentName == 'Spinning Wheel'):
            app.opponentHP -= 20
            app.attack = 'Metal Claw'
        
    app.attackDone = True
    if app.attackDone == True:
        attackByHW(app)
        app.attackDone = False
        app.attackByHWDone = True
    if app.gameOver or app.gameOverWin:
        if event.key == "r":
            appStarted(app)
    if app.myHP <=0 and app.opponentHP <=0:
        app.myHP = 0
        app.opponentHP = 0
        app.gameOverWin = True
        app.attackByHWDone = False
    elif app.myHP <= 0 and (not app.opponentHP <= 0):
        app.myHP = 0
        app.gameOver = True
        app.attackByHWDone = False
    elif app.opponentHP <= 0 and (not app.myHP <= 0):
        app.opponentHP = 0
        app.gameOverWin = True
        app.attackByHWDone = False

def attackByHW(app):
    app.myHP -= 25
    app.attackByHWDone = True
    
def drawMyPokemon(app, canvas):
    canvas.create_image(1*app.width/4, 2.15*app.height/3,
                        image=ImageTk.PhotoImage(app.myPokemonBack))

def cmuBattleMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.backgroundImage2))
    canvas.create_image(3*app.width/4, app.height/3,
                        image=ImageTk.PhotoImage(app.baseBImage))
    canvas.create_image(1*app.width/4, 3*app.height/4,
                        image=ImageTk.PhotoImage(app.baseAImage2))
    drawChoices(app, canvas)
    drawBattleOpponent(app, canvas)
    drawMyPokemon(app, canvas)
    drawHPBoxes(app, canvas)
    drawNames(app, canvas)
    canvas.create_image(app.width/2, 7*app.height/8,
                        image=ImageTk.PhotoImage(app.messageImage2))
    if app.attackByHWDone == True:
        canvas.create_text(app.width/2, 7*app.height/8,
        text=f'{app.opponentName} is resisting against the attack!', font='black')
    if app.gameOver == True:
        canvas.create_text(app.width/2, 7*app.height/8,
        text=f'{app.myName} fainted! You have failed this assignment.', font='black')
        canvas.create_text(app.width/2, 7.3*app.height/8,
        text=f'Press "r" to restart the game.', font='black')
    if app.gameOverWin == True:
        canvas.create_text(app.width/2, 7*app.height/8,
        text=f"{app.opponentName} fainted! Your ditto successfully finished your homework!",
        font='black')
        canvas.create_text(app.width/2, 7.3*app.height/8,
        text=f'Press "r" to restart the game.', font='black')

def drawHPBoxes(app, canvas):
    #opponent's box
    canvas.create_rectangle(2.5*app.width/4, 2*app.height/3, 3.5*app.width/4,
        2.3*app.height/3, fill='white', outline='black', width=1)
    #my box
    canvas.create_rectangle(1*app.width/4, 0.5*app.height/3, 2*app.width/4,
        0.8*app.height/3, fill='white', outline='black', width=1)
    #HP
    canvas.create_rectangle(2.9*app.width/4, 2.1*app.height/3,
        (app.myHP/100*0.5+2.9)*app.width/4, 2.2*app.height/3, 
        fill='green', outline='black',
        width=1)
    canvas.create_rectangle(1.4*app.width/4, 0.6*app.height/3,
        (app.opponentHP/100*0.5+1.4)*app.width/4, 0.7*app.height/3, 
        fill='green', outline='black',
        width=1)
    #"HP"
    canvas.create_text(2.7*app.width/4, 2.15*app.height/3,
    text='HP', fill='black')
    canvas.create_text(1.2*app.width/4, 0.65*app.height/3, 
    text='HP', fill='black')

def drawNames(app, canvas):
    canvas.create_text(3.15*app.width/4, 2.05*app.height/3,
    text=app.myName, fill='black', font='Arial 12 bold')
    canvas.create_text(1.65*app.width/4, 0.55*app.height/3,
    text=app.opponentName, fill='black', font='Arial 12 bold')

###############################################################################

###### CMU Help Mode ######

def cmuHelpMode_redrawAll(app, canvas):
    font = 'Arial 13'
    canvas.create_text(app.width/2, 150, 
                    text='Help', 
                       font='Arial 20 bold', fill='black')
    canvas.create_text(app.width/2, 250, 
    text='Get help from your ditto to win a battle against your assignment.',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 275,
    text="Choose any attack that you think will be effective.",
                        font=font, fill='black')
    canvas.create_text(app.width/2, 300,
    text="If your ditto's HP becomes 0 first, you lose.",
                        font=font, fill='black')
    canvas.create_text(app.width/2, 325,
    text="If your assignment's HP becomes 0 first, you win!",
                        font=font, fill='black')
    canvas.create_text(app.width/2, 350, 
                    text='Press any key to return to the game!',
                       font=font, fill='black')

def cmuHelpMode_keyPressed(app, event):
    app.mode = 'cmuMode'

###############################################################################

def playPokemon():
    runApp(width = 693, height = 672)

playPokemon()
