from create_game import BlackJack


class PlayGame():

    def __init__(self):
        self.game = BlackJack()
        self.begin = 'y'
        answer = input("""Would you like to play a game of BlackJack?
        (y) Yes
        (n) No
        """).lower()
        if answer == self.begin:
            self.game.beginning_draw()
            while True:
                draw_card = 'd'
                compare_hand = 'c'
                user_answer = input("""What would you like to do?
                (d) Draw another Card
                (c) Compare hands
                (e) exit
                """)
                if user_answer == 'e':
                    break
                elif user_answer == draw_card:
                    self.game.draw_card()
                    if self.game.game_end:
                        break
                    self.game.bust_check()
                    if self.game.game_end:
                        break
                    self.game.win_check()
                    if self.game.game_end:
                        break
                elif user_answer == compare_hand:
                    self.game.bust_check()
                    if self.game.game_end:
                        break
                    self.game.compare_hands()
                    if self.game.game_end:
                        break


test = PlayGame()
