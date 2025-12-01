class Player():
    #el jugador tiene que gerstioanr sus cartas y clalcular la puntuacion:)
    def __init__(self, name: str):
        self.hand= [] #-> lista de las cartas
        self.name = name
    
    @property
    def hand(self):
        return self._hand
    @property
    def name(self):
        return self._name


    @hand.setter
    def hand(self,value):
        self._hand=value
    @name.setter
    def name(self,value):
        self._name=value

    def add_card(self, card):
        self._hand.append(card)

    def calculate_score(self):
        addition = 0
        aces = 0
        for card in self.hand:
            val = card.score()
            if val == 11: # YA SE SABE QUE ES UN AS
                aces += 1
            addition += val

        # ajustar segun lop que te dan 
        while addition > 21 and aces > 0:
            addition -= 10
            aces -= 1

        return addition

    def __str__(self):
        cards_str = ", ".join([str(card) for card in self.hand])
        return f"{self.name}: [{cards_str}] - Score: {self.calculate_score()}"