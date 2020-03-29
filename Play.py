import pygame
from board.Board import Board
from board.move import Move
from playsTree import DesicionTree

#initiate tree
tree = DesicionTree(5)

pygame.init()
gameDisplay = pygame.display.set_mode((1000,800))
pygame.display.set_caption("ChessIA")
clock =  pygame.time.Clock()

Board = Board()
Board.createBoard('pta1')
#Board.printBoard()

allTiles = []
allPieces = []
currentPlayer = Board.currentPlayer

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 128)
red = (200, 0, 0)
purple = (102, 0, 102)
light_gray = ((150,150,150))
midle_gray =((120,120,120))
dark_gray = ((70,70,70))




def createSqParams():
    allSqRanges = []
    xMin = 0
    xMax = 100
    yMin = 0
    yMax = 100
    for _ in range(8):
        for _ in range(8):
            allSqRanges.append([xMin, xMax, yMin, yMax])
            xMin += 100
            xMax += 100
        xMin = 0
        xMax = 100
        yMin += 100
        yMax += 100
    return allSqRanges

def squares(x,y,w,h,color):
    pygame.draw.rect(gameDisplay,color,[x,y,w,h])
    allTiles.append([color,[x,y,w,h]])

def drawChessPieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 100
    height = 100
    number = 0

    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, dark_gray)
                if not Board.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load(
                        "./ChessArt/" + Board.gameTiles[number].pieceOnTile.alliance[0].upper() +
                        Board.gameTiles[
                            number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], Board.gameTiles[number].pieceOnTile])
                xpos += 100
            else:
                squares(xpos, ypos, width, height, white)
                if not Board.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load(
                        "./ChessArt/" + Board.gameTiles[number].pieceOnTile.alliance[0].upper() +
                        Board.gameTiles[
                            number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], Board.gameTiles[number].pieceOnTile])
                xpos += 100

            color += 1
            number += 1
        color += 1
        xpos = 0
        ypos += 100


def updateChessPieces():

    xpos = 0
    ypos = 0
    number = 0
    newPieces = []

    for _ in range(8):
        for _ in range(8):
            if not Board.gameTiles[number].pieceOnTile.toString() == "-":

                img = pygame.image.load(
                    "./ChessArt/" + Board.gameTiles[number].pieceOnTile.alliance[0].upper() + Board.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                img = pygame.transform.scale(img, (100, 100))

                newPieces.append([img, [xpos, ypos], Board.gameTiles[number].pieceOnTile])
            xpos += 100
            number += 1
        xpos = 0
        ypos += 100

    return newPieces


allSqParams = createSqParams()
drawChessPieces()



selectedImage = None
selectedLegals = None
resetColors = []
quitGame = False
mx, my = pygame.mouse.get_pos()
prevx, prevy = [0,0]

while not quitGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selectedImage==None:
                mx, my = pygame.mouse.get_pos()
                for piece in range(len(allPieces)):
                    if allPieces[piece][2].alliance == currentPlayer:
                        ##print(piece)
                        ##print('Is current player')
                        if allPieces[piece][1][0] < mx < allPieces[piece][1][0] + 100:
                            if allPieces[piece][1][1] < my < allPieces[piece][1][1] + 100:
                                ##Se decide cual es la pieza que se toco
                                selectedImage = piece
                                prevx = allPieces[piece][1][0]
                                prevy = allPieces[piece][1][1]

                                #print('Select piece: ')
                                #print(allPieces[selectedImage][2].toString())
                                #print(1+prevx//100) #--X
                                #print(1+prevy//100) #--Y

                                selectedLegals = allPieces[selectedImage][2].calculateLegalMoves(Board)
                                for legals in selectedLegals:
                                    resetColors.append([legals, allTiles[legals][0]])


                                    if allTiles[legals][0] == dark_gray:
                                        allTiles[legals][0] = midle_gray
                                    else:
                                        allTiles[legals][0] = light_gray


        #Si se selecciono una piesa
        if event.type == pygame.MOUSEMOTION and not selectedImage == None:
            mx, my = pygame.mouse.get_pos()
            if mx<800:
                allPieces[selectedImage][1][0] = mx-50
                allPieces[selectedImage][1][1] = my-50


        if event.type == pygame.MOUSEBUTTONUP:
            for resets in resetColors:
                allTiles[resets[0]][0] = resets[1]

            try:
                pass
            except:
                pass




    gameDisplay.fill((255, 255, 255))
    pygame.draw.rect(gameDisplay, dark_gray, [800, 0, 2, 800])

    for info in allTiles:
        pygame.draw.rect(gameDisplay, info[0], info[1])

    for img in allPieces:
        gameDisplay.blit(img[0], img[1])

    pygame.display.update()
    clock.tick(60)
