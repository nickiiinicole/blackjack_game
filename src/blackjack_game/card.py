class Card():
    #suit es el palo->mano, para identificar : corazoned, diamantes, picas, treboles
    # rango-> valor de la de carta
    def __init__(self, suit, rank, point):
        self.suit= suit
        self.rank= rank
    
    @property
    def suit(self):
        return self._suit
    @property
    def rank(self):
        return self._rank
    @property
    def point(self):
        return self._point

    @suit.setter
    def suit(self, value: str):
        valid_suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
        if value not in valid_suits:
            raise ValueError(f"Invalid suit: {value}. Must be valid {valid_suits}")
        self._suit = value
        
    @rank.setter
    def rank(self, value: str):
        valid_ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J'}
        if value not in valid_ranks:
            raise ValueError(f"Invalid rank: {value}. Must be valid {valid_ranks}")
        self._rank = value

    def score(self):
        if self.rank in {'K,Q,J'}:
            return 10
        if self.rank == 'A':
            return [1,11]
        return int(self.rank)
    
    def __str__(self): 
        return f"{self.rank} of {self.suit}"
        
    