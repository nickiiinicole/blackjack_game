import random
from card import Card
from player import Player

class Game():
    def __init__(self):
        self.deck = []
        self.player = Player("NICKIIII")
        self.dealer = Player("Dealer")
        self._create_deck()
    
    def _create_deck(self):
        #rellenamos la baraja
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [Card(s, r) for s in suits for r in ranks]

    def start_game(self):
        print("--- STARTING BLACKJACK :D---")
        random.shuffle(self.deck) # Barajar

        # PRIMERO SE REPAte dos carticas
        for _ in range(2):
            self.player.add_card(self.deck.pop())
            self.dealer.add_card(self.deck.pop())

        # mostramos que carta tiene
        print(self.dealer.name + " shows: " + str(self.dealer.hand[0]) + ", [Hidden]")
        print(self.player)

        # player
        self.player_turn()

        # ahroa turno dealer
        player_score = self.player.calculate_score()
        if player_score <= 21:
            self.dealer_turn()
        
        self.check_winner()

    def player_turn(self):
        playing = True 

        while playing:
            # puntuacion actuañ
            score = self.player.calculate_score()

            # Si ya tiene 21 o más, se acaba el turno automatic.
            if score >= 21:
                playing = False
            
            # ahora le pregutnamos is quiere msotrar 
            else:
                choice = input("\nDo you want to (H)it or (S)tand? ").upper()
                
                if choice == 'S':
                    # Segunda condición de salida: El jugador queire mnoistar
                    playing = False
                
                elif choice == 'H':
                    # pedimos carta
                    new_card = self.deck.pop()
                    print(f"You drew: {new_card}")
                    self.player.add_card(new_card)
                    print(self.player)
                
                else:
                    print("Invalid option. Please choose 'H' or 'S'.")

    def dealer_turn(self):
        print("\n--- Dealer's Turn ---")
        print(self.dealer)
        # -->El dealer pide hasta llegar a 17
        while self.dealer.calculate_score() < 17:
            new_card = self.deck.pop()
            print(f"Dealer drew: {new_card}")
            self.dealer.add_card(new_card)
            print(f"Dealer score: {self.dealer.calculate_score()}")

    def check_winner(self):
        print("\n--- FINAL RESULTS ---")
        p_score = self.player.calculate_score()
        d_score = self.dealer.calculate_score()

        print(f"Final Scores -> You: {p_score} | Dealer: {d_score}")

        if p_score > 21:
            print("BUST! You went over 21. Dealer wins.")
        elif d_score > 21:
            print("Dealer BUST! You win!")
        elif p_score > d_score:
            print("You win!")
        elif d_score > p_score:
            print("Dealer wins.")
        else:
            print("It's a Tie (Push)!")

# para ejrcuta
if __name__ == "__main__":
    game = Game()
    game.start_game()



