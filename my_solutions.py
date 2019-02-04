# This is the code
class card():
    """This creates a card object"""
    rank_names = [None, 'Ace', '2', '3', '4', '5', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    def __init__(self, rank = 0, suit = 2):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"The rank is {card.rank_names[self.rank]} and the suit is {card.suit_names[self.suit]}"

ace_of_spade = card(1, 3)
print(ace_of_spade)

# inside class card

def __lt__(self, other):
    #check the suits
    if self.suit < other.suit: return True
    if self.suit > other.suit: return False

    #suits are the same...check ranks
    return self.rank < other.rank

#inside class card:

def __eq__(self, other):
    return self.rank == other.rank and self.suit == other.suit

class Deck:
    def __init__(self):
        self.card = []
        for suit in range(4):
            for rank in range(1, 14):
                Card = card(suit, rank)
                self.cards.append(card)
    def pop_card(self):
        pass
