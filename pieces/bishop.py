from pieces.piece import Piece

class Bishop(Piece):

    alliance = None
    position = None

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position


    def toSting(self):
        pass
