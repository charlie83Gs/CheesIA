import pygame
from board.Board import Board

pygame.init()
gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption("ChessIA")
clock =  pygame.time.Clock()

Board = Board()
Board.createBoard('pta1')
Board.printBoard()



##Ciclo del juego , mientras quitGame sea falso la ventana se mantiene abierta##
quitGame = False

while not quitGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)
