import random
class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        if not self.cards:
            return None
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_card(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def deal_hands(self,hands,hands_each):
        num_per_hand = len(self.cards)
        if hands*hands_each > num_per_hand:
            print("Cannot deal many cards")
        hands = []
        for _ in range(hands):
            hand = Hand()
            for _ in range(hands_each):
                card = self.deal_card()
                if card:
                    hand.add_card(card)
            hands.append(hand)
        return hands
                

class Hand(Deck):
    def __init__(self,label=''):
        self.cards = []
        self.label = label


deck = Deck()
#deck.sort()
#print(deck)
hand = Hand('new hand')
hand.cards
hands = deck.deal_hands(10,10)
for i, hand in enumerate(hands):
    print(f"Hand {i+1}: {hand}")


