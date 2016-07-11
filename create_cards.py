

class Card:

    def __init__(self):
        import random
        self.suits = ['♠', '♥', '♣', '♦']
        self.suit = random.choice(self.suits)
        valuelist = ['J', 'Q', 'K']
        value = random.randint(1, 10)
        self.value = 0
        if 10 > value > 1:
            self.value = value
        elif value == 10:
            self.value = random.choice(valuelist)
        elif value == 1:
            self.value = 'A'
        self.card_value = [self.suit, self.value]

    def __repr__(self):
        return str(self.card_value)
