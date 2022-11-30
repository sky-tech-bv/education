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
            self.dealer_list = self.cards_player_has[1:]
            print('The Dealer has the following cards: ')
            counter = 1
            for card in self.dealer_list:
                print(str(counter) + '. ' + str(card) + f'. It\'s costs {card.value} points.')
                counter += 1
            print('The Dealer also has one hidden card.') 
        else:
            print(f'The {self.name} has the following cards: ')
            counter = 1
            for card in self.cards_player_has:
                print(str(counter) + '. ' + str(card) + f'. It\'s costs {card.value} points.')
                counter += 1
                
    def take_current_score(self):
        current_score = 0
        minus = False
        for item in self.cards_player_has:
            current_score += item.value
            if current_score > 21:
                if item.rank == 'Ace':
                    minus = True
        if minus:
            current_score = current_score - 10
        return current_score
                    
    def show_result(self):
        print(f'The {self.name} has the following cards: ')
        counter = 1
        score = 0
        nimus = False
        for card in self.cards_player_has:
            print(str(counter) + '. ' + str(card) + f'. It\'s costs {card.value} points.')
            counter += 1
            score += card.value
            if card.rank == 'Ace':
                nimus = True
        if nimus:
            score = score - 10
        print(f'The total score for {self.name} is {score}.')
        return score
    
                
class Game:
    def __init__(self, retry = True):
        self.retry = retry
        
    def start_display(self):
        if self.retry:
            print('This is a simple simulator of BLACK JACK game. There are a lack of real game rules.')
            print('We play this game without any rates of money.')
            print('So, to get accuinted with actual game rules, please read the following list:')
            print('1. In this game player games against the computer or Dealer player.')
            print('2. To win the game you must get greater score then a Dealer or get score equeal 21.')
            print('Ohh... all the rules you can find with google search.')
            
        else:
            print('The second time is easier to play the game! Good luck!')
            print('P.S. We won\'n remind you the game rules.')

def main():               
    first_deck = Deck()
    begining = is_continue()
    game1 = Game()
    counter_game = 1
    name = input('For continue gaming please enter your name: ')
    while begining:
        if counter_game >= 2:
            game1 = Game(False)
        counter_game += 1
        game1.start_display()
        player1 = Player(name)
        dealer = Player()
        first_deck.shuffle_deck()
        give_a_card(player1, first_deck, 2)
        give_a_card(dealer, first_deck, 2)
        for i in range(10):
            show_game_desc(player1, dealer)
            black_jack_palyer = check_black_jack(player1)
            black_jack_dealer = check_black_jack(dealer)
            if black_jack_dealer == 1:
                if black_jack_palyer == 1:
                    print('It\'s a tie! No one has won!')
                else:
                    print('Dealer won!')
                begining = is_continue(1)
                break
            if check_player_lose(player1):
                begining = is_continue(1)
                break
            answer = take_next_step()
            if answer == 0:
                if dealer.take_current_score() < 17 :
                    give_a_card(dealer, first_deck, 1)
                    continue
                else:
                    continue
            if answer == 1:
                give_a_card(player1, first_deck, 1)
                if dealer.take_current_score() < 17 :
                    give_a_card(dealer, first_deck, 1)
                    continue
                else:
                    continue
                
            if answer == 2:
                dealer_score = dealer.show_result()
                print('')
                player1_score = player1.show_result()
                print('')
                if player1_score > dealer_score and player1_score <= 21:
                    print(f'{player1.name} has won!')
                    begining = is_continue(1)
                    break
                elif player1_score < dealer_score and dealer_score <=21:
                    print(f'{dealer.name} has won!')
                    begining = is_continue(1)
                    break
                elif player1_score > 21:
                    print(f'{dealer.name} has won!')
                    begining = is_continue(1)
                    break
                else:
                    print(f'{player1.name} has won!')
                    begining = is_continue(1)
                    break
                
def is_continue(arg = 0):
    answer = 'WRONG'
    while answer not in ['Y', 'N']: 
        if arg == 0: 
            answer = input('Are you ready to start game? Enter Y or N: ')
        if arg != 0:
            answer = input('Do you want to play again? Enter Y or N: ')
        if answer.isdigit():
            print('You entered the number! Please try again.')
            continue
        if answer.upper() not in ['Y', 'N']:
            print('You entered the wrong item! Please try again.')
            continue
        if answer.upper() == 'Y':
            return True
        else:
            return False
        
def give_a_card(player, deck, cards_count):
    for i in range(cards_count):
        player.add_cards(deck.give_one_card())
        
def show_game_desc(player1, player2):
    print('It\'s the curent game table:')
    player2.show_cards()
    print('')
    player1.show_cards()
    print('')
    
def take_next_step():
    answer = 'Wrong'
    while answer not in ['pass', 'card', 'open']:
        print('Enter what you want to do: give one more card - <card>, pass next step - <pass>')
        answer = input('and finish the game and know who is winner - <open>: ')
        if answer.lower() not in ['pass', 'card', 'open']:
            print('You entered the wrong item. Please enter the correct item.')
            continue
        if answer.lower() == 'pass':
            return 0
        elif answer.lower() == 'card':
            return 1
        else:
            return 2
    
def check_black_jack(player):
    if player.take_current_score() == 21:
        print(f'{player.name} has 21! He has Black Jack!')
        return 1
    else:
        return 0
    
def check_player_lose(player):
    if player.take_current_score() > 21:
        print(f'{player.name} lose the game!')
        return True
    else:
        return False
    
if __name__ == '__main__':
    main()



        


