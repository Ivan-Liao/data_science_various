class Card():
    """
    Card Class.
    
    Attributes:
        rank - e.g. 'A', '2', '3', 'K'
        suit - e.g. 'C' (clubs)
        face_up_bool - whether card is face up or not
    """
    
    def __init__(self, rank, suit, face_up_bool=True):
        self.rank = rank
        self.suit = suit
        self.face_up_bool = face_up_bool
        