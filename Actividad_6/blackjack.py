import random

# Clase para representar una carta
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

# Clase para representar una baraja
class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Corazón', 'Trébol', 'Diamante', 'Espada']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Clase para representar una mano de cartas
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0

        for card in self.cards:
            value += card.value()
            if card.rank == 'A':
                num_aces += 1

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

# Clase para representar al jugador
class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 100

    def bet(self):
        while True:
            try:
                bet_amount = int(input(f"{self.name}, ¿cuántas fichas deseas apostar? (Tienes {self.chips} fichas disponibles): "))
                if bet_amount < 1 or bet_amount > self.chips:
                    print("Apuesta inválida. Debes apostar entre 1 y", self.chips, "fichas.")
                else:
                    self.chips -= bet_amount
                    return bet_amount
            except ValueError:
                print("Por favor, ingresa una cantidad válida.")

# Función para mostrar la mano de un jugador
def show_hand(player_name, hand):
    print(f"{player_name}'s mano:")
    for card in hand.cards:
        print(card)
    print(f"Puntuación total: {hand.get_value()}")

# Función para jugar una partida de Blackjack
def play_blackjack():
    print("¡Bienvenido al Juego de Blackjack!")
    player_name = input("Por favor, ingresa tu nombre: ")
    player = Player(player_name)

    while player.chips > 0:
        print(f"\n{player.name}, tienes {player.chips} fichas disponibles.")
        bet_amount = player.bet()

        # Inicializar la baraja y las manos del jugador y la casa
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        # Repartir las primeras dos cartas a cada jugador
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        show_hand(player.name, player_hand)
        print(f"Carta de la casa:\n{dealer_hand.cards[0]}")

        # Verificar si el jugador tiene blackjack
        if player_hand.get_value() == 21:
            print("¡Blackjack! ¡Ganaste esta mano!")
            player.chips += 2 * bet_amount
        else:
            # Turno del jugador
            while player_hand.get_value() < 21:
                action = input("¿Quieres pedir carta (P) o plantarte (PL)? ").upper()

                if action == 'P':
                    player_hand.add_card(deck.deal_card())
                    show_hand(player.name, player_hand)
                elif action == 'PL':
                    break

            # Turno de la casa
            print("Turno de la casa...")
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal_card())

            show_hand(player.name, player_hand)
            show_hand("Casa", dealer_hand)

            # Determinar el ganador
            if dealer_hand.get_value() > 21 or (player_hand.get_value() > dealer_hand.get_value() and player_hand.get_value() <= 21):
                print(f"{player.name} ¡Ganaste esta mano!")
                player.chips += 2 * bet_amount
            elif dealer_hand.get_value() == player_hand.get_value():
                print("Empate. Se te devuelve tu apuesta.")
                player.chips += bet_amount
            else:
                print("Casa gana. Pierdes tu apuesta.")
        
        # Verificar si el jugador desea seguir jugando
        if player.chips > 0:
            play_again = input(f"{player.name}, ¿quieres jugar otra mano? (S/N): ").upper()
            if play_again != 'S':
                break
        else:
            print("Te quedaste sin fichas. Juego terminado.")
            break

    print("Gracias por jugar al Blackjack, ¡hasta la próxima!")

if __name__ == "__main__":
    play_blackjack()