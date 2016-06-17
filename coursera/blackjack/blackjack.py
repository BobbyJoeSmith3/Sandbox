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
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        ans = "Hand contains "
        for card in self.cards:
            ans += str(card) + " "
        return ans

    def add_card(self, card):
        # add a card object to a hand
        return self.cards.append(card)

    def get_value(self):
        # NOTE: count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust

        # check for aces
        has_ace = False
        for card in self.cards:
            if VALUES.get(card.get_rank()) == 1:
                has_ace = True
        # compute the value of the hand
        hand_value = 0
        for card in self.cards:
            hand_value += VALUES.get(card.get_rank())
        if has_ace == False:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value


    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards


# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.card_deck = []

        for suit in SUITS:
            for rank in RANKS:
                # create a Card object using Card(suit, rank) and add it to the card list for the deck
                self.card_deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck
        return random.shuffle(self.card_deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.card_deck.pop()

    def __str__(self):
        # return a string representing the deck
        ans = "Deck contains "
        for card in self.card_deck:
            ans += str(card) + " "
        return ans



#define event handlers for buttons
def deal():
    global outcome, in_play, new_deck, player_hand, dealer_hand

    in_play = True

    # shuffle deck
    new_deck = Deck()
    new_deck.shuffle()

    # deal player hand and dealer hand
    player_hand = Hand()
    dealer_hand = Hand()
    i = 0
    while i < 2:
        player_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())
        i += 1

    print "Player hand contains", player_hand, "with a hand value of", player_hand.get_value()
    print "Dealer hand contains", dealer_hand, "with a hand value of", dealer_hand.get_value()

def hit():
    global in_play, player_hand, score, outcome, new_deck
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(new_deck.deal_card())
        # calculate value and print to screen
        print "Player's hand value =", player_hand.get_value()
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21:
        outcome = player_hand.get_value(), "- You busted!"
        score -= 1
        print outcome
        print "Score =", score

def stand():
    pass	# replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below

    card = Card("S", "A")
    card.draw(canvas, [300, 300])


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
