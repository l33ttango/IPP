# http://www.codeskulptor.org/#user40_DDHAalLZaBTzgMH.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player_hand = []
dealer_hand = []


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []


    def __str__(self):
        # return a string representation of a hand
        cards_in_hand = "Hand contains "
        for card in self.hand:
            cards_in_hand += str(card.suit) + str(card.rank) + " "
            return cards_in_hand

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)


    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_sum = 0
        card_ranks = []
        for card in self.hand:
            card_ranks.append(card.get_rank())
            hand_sum += VALUES[card.get_rank()]        
        if hand_sum + 10 <= 21 and 'A' in card_ranks:
            hand_sum += 10
        return hand_sum
    
    def draw(self, canvas, pos):        
        # draw a hand on the canvas, use the draw method for cards
        for i, card in enumerate(self.hand):
            card.draw(canvas, [pos[0] + 75 * i, pos[1]])
         
        
# define deck class 
class Deck:
    # create a Deck object
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
                
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(0)
    
    def __str__(self):
        # return a string representing the deck
        my_new_deck = "Deck contains "
        for card in self.deck:
            my_new_deck += str(card) + " "
        return my_new_deck




#define event handlers for buttons
def deal():
    global outcome, in_play, playing_deck, dealer_hand, player_hand, score
    if in_play: 
        score -= 1
    
    in_play = True
    playing_deck = Deck()
    playing_deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    dealer_hand.add_card(playing_deck.deal_card())
    dealer_hand.add_card(playing_deck.deal_card())
    player_hand.add_card(playing_deck.deal_card())
    player_hand.add_card(playing_deck.deal_card())
    outcome = "Hit or Stand?"
        
    

def hit():
    # if the hand is in play, hit the player   
    # if busted, assign a message to outcome, update in_play and score
    global in_play, player_hand, playing_deck, outcome, score
    if in_play:
        player_hand.add_card(playing_deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = "Player busts! Deal?"
            in_play = False
            score -= 1

        
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global in_play, dealer_hand, playing_deck, outcome, score
    if in_play:
        if dealer_hand.get_value() >= 17:
            if dealer_hand.get_value() > 21:
                outcome = "Dealer busts! New Deal?"
                in_play = False
                score += 1
                return
            elif player_hand.get_value() > dealer_hand.get_value():
                outcome = "You win! New Deal?"
                in_play = False
                score += 1
                return 
            else:
                outcome = "Dealer wins! New Deal?"
                in_play = False
                score -= 1
                return
        elif dealer_hand.get_value() >= player_hand.get_value():
                outcome = "Dealer wins! New Deal?"
                in_play = False
                score -= 1
                return
        else:
            dealer_hand.add_card(playing_deck.deal_card())
            return stand()         
   

# draw handler    
def draw(canvas):
    
    dealer_hand.draw(canvas, [75, 200])
    player_hand.draw(canvas,[75, 400])
    canvas.draw_text(outcome, (100, 360), 50, "White")
    canvas.draw_text("Score = " + str(score), (420, 100), 35, "White")
    canvas.draw_text("Blackjack", (50, 100), 35, "White")
    canvas.draw_text("Dealer", (5, 250), 20, "White")
    canvas.draw_text("Player", (5, 450), 20, "White")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, 
                          CARD_BACK_SIZE, [75 + 36 , 200 + 48], CARD_BACK_SIZE)
        

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
