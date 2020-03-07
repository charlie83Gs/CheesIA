from board.tile import Tile
from pieces.nullPiece import NullPiece
from pieces import bishop
from pieces import king
from pieces import knight
from pieces import pawn
from pieces import queen
from pieces import rook



class Board:

    gameTiles = {}

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
                    for x in range(2,18):
                        if(line[x] != '|'):
                            count += 1
                            ##print(count,line[x])
                            self.loadPieces(count,line[x])

        file1.close()

    def loadPieces(self,n,p):
        if(p=='K'):
            self.gameTiles[n] = Tile(n, king.King("Black", n))
        elif(p=='k'):
            self.gameTiles[n] = Tile(n, king.King("White", n))
        elif(p=='Q'):
            self.gameTiles[n] = Tile(n, queen.Queen("Black", n))
        elif(p=='q'):
            self.gameTiles[n] = Tile(n, queen.Queen("White", n))
        elif(p=='N'):
            self.gameTiles[n] = Tile(n, knight.Knight("Black", n))
        elif(p=='n'):
            self.gameTiles[n] = Tile(n, knight.Knight("White", n))
        elif(p=='B'):
            self.gameTiles[n] = Tile(n, bishop.Bishop("Black", n))
        elif(p=='b'):
            self.gameTiles[n] = Tile(n, bishop.Bishop("White", n))
        elif(p=='R'):
            self.gameTiles[n] = Tile(n, rook.Rook("Black", n))
        elif(p=='r'):
            self.gameTiles[n] = Tile(n, rook.Rook("White", n))
        elif(p=='P'):
            self.gameTiles[n] = Tile(n, pawn.Pawn("Black", n))
        elif(p=='p'):
            self.gameTiles[n] = Tile(n, pawn.Pawn("White", n))
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












