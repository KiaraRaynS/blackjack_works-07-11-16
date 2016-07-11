from create_player import Person, Dealer
from create_cards import Card
# Still need to work logic on how to prevent duplicate cards


class BlackJack():

    def __init__(self):
        self.game_end = False
        # To break game have an if game_end = true:
        # break
        self.player = Person()
        self.dealer = Person()
        self.used_cards = []
        self.players_hand = []
        self.dealers_hand = []

    def draw_card_player(self):
        new_card = Card()
        card_value = new_card.card_value
        # Check if card in hand
        while card_value in self.used_cards:
            new_card = Card()
            card_value = new_card.card_value
        else:
            self.player.hand.append(card_value)
            self.used_cards.append(card_value)
            self.player.card_values.append(card_value[1])

    def draw_card_dealer(self):
        new_card = Card()
        card_value = new_card.card_value
        # Check if card in hand
        while card_value in self.used_cards:
            new_card = Card()
            card_value = new_card.card_value
        else:
            self.dealer.hand.append(card_value)
            self.used_cards.append(card_value)
            self.dealer.card_values.append(card_value[1])

    def beginning_draw(self):
        # dealer draws
        self.draw_card_dealer()
        self.draw_card_dealer()
        print('Dealer Hand')
        print(self.dealer.hand[1])
        # player draws
        self.draw_card_player()
        self.draw_card_player()
        for item in self.player.hand:
            self.used_cards.append(item)
        print('Player Hand')
        print(self.player.hand)

    def draw_card(self):
        dealer_hand_value = self.dealer.calculate_hand_value()
        player_hand_value = self.player.calculate_hand_value()
        if dealer_hand_value < 17:
            self.draw_card_dealer()
            print('Dealers Hand')
            print(self.dealer.hand[1])

        if player_hand_value < self.player.max_hand_value:
            self.draw_card_player()
            print('Your Hand')
            print(self.player.hand)

    def win_check(self):
        dealer_value = self.dealer.calculate_hand_value()
        player_value = self.player.calculate_hand_value()
        if dealer_value and player_value == 21:
            print('Draw!')
            print('Dealer Hand')
            print(self.dealer.hand)
            print('Your Hand')
            print(self.player.hand)
            self.game_end = True
            return self.game_end
        elif dealer_value == 21:
            print('Dealer wins!')
            print('Dealer Hand')
            print(self.dealer.hand)
            print('Your Hand')
            print(self.player.hand)
            self.game_end = True
            return self.game_end
        elif player_value == 21:
            print('Congradulations, you win!')
            print('Dealer Hand')
            print(self.dealer.hand)
            print('Your Hand')
            print(self.player.hand)
            self.game_end = True
            return self.game_end

    def bust_check(self):
        dealer_value = self.dealer.calculate_hand_value()
        player_value = self.player.calculate_hand_value()
        if player_value > 21 and dealer_value > 21:
            print('Draw!')
            print('Dealer Hand')
            print(self.dealer.hand)
            print('Your Hand')
            print(self.player.hand)
            self.game_end = True
            return self.game_end
        elif dealer_value > 21:
            print('Congradulations, you win!')
            print("Dealer hand")
            print(self.dealer.hand)
            print('Your hand')
            print(self.player.hand)
            self.game_end = True
            return self.game_end
        elif player_value > 21:
            print('Dealer wins!')
            print('Dealer hand')
            print(self.dealer.hand)
            print('Your hand')
            print(self.player.hand)
            self.game_end = True
            return self.game_end

    def compare_hands(self):
        dealer_value = self.dealer.calculate_hand_value()
        while dealer_value < 17:
            self.draw_card_dealer()
            dealer_value = self.dealer.calculate_hand_value()
            self.bust_check()
        player_value = self.player.calculate_hand_value()
        if dealer_value == player_value:
            print('Draw!')
            print('Dealers Hand')
            print(self.dealer.hand)
            print('Your Hand')
            print(self.player.hand)
        if dealer_value > player_value:
            print('Dealer wins!')
            print('Dealers Hand')
            print(self.dealer.hand)
            print('Your Hand')
            print(self.player.hand)
            self.game_end = True
            return self.game_end

        if dealer_value < player_value:
            print('Congradulations, you win!')
            print('Dealers hand')
            print(self.dealer.hand)
            print('Your hand')
            print(self.player.hand)
            self.game_end = True
            return self.game_end
