import pygame
from board.Board import Board

pygame.init()
gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption("ChessIA")
clock =  pygame.time.Clock()

Board = Board()
Board.createBoard('pta1')
#Board.printBoard()

allTiles = []
allPieces = []
currentPlayer = Board.currentPlayer


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
    black = (0,0,0)
    white = (255, 255, 255)
    blue = (0, 0, 128)
    red = (200, 0, 0)
    purple = (102, 0, 102)
    number = 0
    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, blue)
                if not Board.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load(
                        "./ChessArt/" + Board.gameTiles[number].pieceOnTile.alliance[0].upper() +
                        Board.gameTiles[
                            number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], Board.gameTiles[number].pieceOnTile])
                xpos += 100
            else:
                squares(xpos, ypos, width, height, red)
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




    gameDisplay.fill((255, 255, 255))

    for info in allTiles:
        pygame.draw.rect(gameDisplay, info[0], info[1])

    for img in allPieces:
        gameDisplay.blit(img[0], img[1])

    pygame.display.update()
    clock.tick(60)
