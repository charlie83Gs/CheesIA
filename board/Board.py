from board.tile import Tile
from pieces.nullPiece import NullPiece
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook



class Board:

    ##Lista que almacena todas las piezas del tablero
    gameTiles = {}
    ##Jugador que inicia jugando
    currentPlayer = None

    def __init__(self):
        pass


    def createBoard(self,filename):
        file1 = open('BoardFiles/'+filename+'.cfl', 'r')
        count = -1
        while True:
            line = file1.readline()
            if not line:
                break
            if line[0] != '#':
                if line != '\n':
                    if line[0] == 'W' or line[0] == 'B' :
                        self.currentPlayer = line[0:5]
                    else:
                        for x in range(2,18):
                            if(line[x] != '|'):
                                count += 1
                                #print(count,line[x])
                                self.loadPieces(count,line[x])

        file1.close()

    def loadPieces(self,n,p):
        if(p=='K'):
            self.gameTiles[n] = Tile(n, King("Black", n))
        elif(p=='k'):
            self.gameTiles[n] = Tile(n, King("White", n))
        elif(p=='Q'):
            self.gameTiles[n] = Tile(n, Queen("Black", n))
        elif(p=='q'):
            self.gameTiles[n] = Tile(n, Queen("White", n))
        elif(p=='N'):
            self.gameTiles[n] = Tile(n, Knight("Black", n))
        elif(p=='n'):
            self.gameTiles[n] = Tile(n, Knight("White", n))
        elif(p=='B'):
            self.gameTiles[n] = Tile(n, Bishop("Black", n))
        elif(p=='b'):
            self.gameTiles[n] = Tile(n, Bishop("White", n))
        elif(p=='R'):
            self.gameTiles[n] = Tile(n, Rook("Black", n))
        elif(p=='r'):
            self.gameTiles[n] = Tile(n, Rook("White", n))
        elif(p=='P'):
            self.gameTiles[n] = Tile(n, Pawn("Black", n))
        elif(p=='p'):
            self.gameTiles[n] = Tile(n, Pawn("White", n))
        else:
            self.gameTiles[n] = Tile(n,NullPiece())



    def printBoard(self):
        count = 0
        for tiles in range(64):
            print('|',end=self.gameTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('|', end ='\n')
                count = 0












