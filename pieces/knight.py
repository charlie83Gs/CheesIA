from pieces.piece import Piece

class Knight(Piece):

    alliance = None
    position =  None

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position

    def toSting(self):
        return "B" if self.alliance == "Black" else "b"