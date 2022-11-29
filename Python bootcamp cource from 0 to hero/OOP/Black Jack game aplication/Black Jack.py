import random
# Create a global variables to discribe all cards in deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Write a class to create each cards in deck
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f'It\'s a {self.rank} of {self.suit}'
    
# Write a class to create a deck
class Deck:
    def __init__(self):
        self.all_cards_in_deck = []
        for suit in suits:
            for rank in ranks:
                self.all_cards_in_deck.append(Card(suit, rank))
                
    def give_one_card(self):
        return self.all_cards_in_deck.pop()
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards_in_deck)
        
        
# Write a class to create a player
class Player:
    def __init__(self, name = 'Dealer'):
        self.name = name
        self.cards_player_has = []
        
    def add_cards(self, cards):
        if type(cards) == type([]):
            self.cards_player_has.extend(cards)
        else:
            self.cards_player_has.append(cards)
            
    def show_cards(self):
        if self.name == 'Dealer':
            print(self.cards_player_has[-1].value)       
            
first_deck = Deck()
player1 = Player('gamer')
dealer = Player()
first_deck.shuffle_deck()



        


