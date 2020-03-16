
#evaluator adapted for any position
class BoardEvaluator:

    def __init__(self):
        pass

    def evaluate(self, player, board, depth):
        
        if(player == "White"):
            return self.scorePlayer("White", board) - self.scorePlayer("Black", board)
        else:
            return self.scorePlayer("Black", board) - self.scorePlayer("White", board)
        
        #print(self.scorePlayer("White", board) - self.scorePlayer("Black", board))

    def scorePlayer(self, player, board):
        return self.pieceValue(player, board)

    def pieceValue(self, player, board):
        pieceValues = 0
        myPieces = board.calculateActivePieces(player)

        for piece in myPieces:
            pieceValues += piece.value

        return pieceValues