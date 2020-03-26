from board.Board import Board




class Move:
    board = None
    movedPiece = None
    destination = None

    def __init__(self, board, movePiece, destination):
        self.board = board
        self.movedPiece = movePiece
        self.destination = destination

    def createNewBoard(self):
        newBoard = Board()
        gameTiles = {}

        # TODO CHECK if enpassant attack
        enpassLocation = None
        if self.movedPiece.toString() == 'P':
            pass
        elif self.movedPiece.toString() == 'p':
            pass