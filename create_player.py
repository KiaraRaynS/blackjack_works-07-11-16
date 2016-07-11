from create_cards import Card


class Person():

    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.card_values = []
        self.max_hand_value = 21
        self.used_cards = []

    def calculate_hand_value(self):
        jqk = ['J', 'Q', 'K']
        current_value = 0
        hand_int_values = []
        integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ace_in_hand = False
        for value in self.card_values:
            if value in integers:
                hand_int_values.append(value)
            if value in jqk:
                hand_int_values.append(10)
            if value == 'A':
                ace_in_hand = True
        current_value = sum(hand_int_values)
        if ace_in_hand:
            if current_value + 11 <= 21:
                current_value + 11
            else:
                current_value + 1
        self.hand_value = current_value
        return self.hand_value


class Dealer(Person):

    def __init__(self):
        super().__init__()
        self.max_hand_value = 17
