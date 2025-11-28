class Player():
    #el jugador tiene que gerstioanr sus cartas y clalcular la puntuacion:)
    def __init__(self, hand, score):
        self.hand= hand #-> lista de las cartas
        self.score = score

    @property
    def hand(self):
        return self.hand
    
    @property
    def score(self):
        return self.score
    
    @hand.setter
    def hand(self,value):
        self._hand=value

    @score.setter
    def score(self,value:int):
        self._score=value

    def addition_hand(self):
        addition = 0
        aces = 0
        for card in self.hand:
            value = card.score()
            if card.rank == 'A':
                aces += 1
                addition += 11
            else:
                addition += value

        # AJUSTAR LOS ASES
        while addition > 21 and aces > 0:
            addition -= 10   # convertir un As de 11 EN 1
            aces -= 1

        return addition
