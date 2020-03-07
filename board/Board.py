from board.tile import Tile
from pieces.nullPiece import NullPiece


class Board:

    gameTiles = {}

    def __init__(self):
        pass

    def createBoard(self):
        for tile in range(64):
            self.gameTiles[tile] = Tile(tile,NullPiece())

    def printBoard(self):
        count = 0
        for tiles in range(64):
            print('|',end=self.gameTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('|', end ='\n')
                count = 0
