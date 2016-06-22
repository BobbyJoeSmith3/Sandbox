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
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
in_play = False
outcome = ""
prompt = ""
score = 0
first_round = True

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
        ans = ""
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
        # draw a hand on the canvas, use the draw method for cards
        for c in self.cards:
            c.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 5



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
    global outcome, in_play, my_deck, player_hand, dealer_hand, player_busted, first_round, prompt

    in_play = True
    player_busted = False

    # shuffle deck
    my_deck = Deck()
    my_deck.shuffle()

    # create hand objects for dealer and player
    player_hand = Hand()
    dealer_hand = Hand()

    # deal cards to player and dealer hands
    i = 0
    while i < 2:
        player_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        i += 1

    # format print message based on whether it's the first round
    if first_round:
        prompt = "Hit or stand?"
        print "Player hand contains", str(player_hand) + "for a hand value of", player_hand.get_value()
        print "Dealer hand contains", str(dealer_hand) + "for a hand value of", dealer_hand.get_value()
        first_round = False
    else:
        prompt = "Hit or stand?"
        print "\n\nPlayer hand contains", str(player_hand) + "for a hand value of", player_hand.get_value()
        print "Dealer hand contains", str(dealer_hand) + "for a hand value of", dealer_hand.get_value()



def hit():
    global in_play, player_hand, score, outcome, my_deck, player_busted, prompt

    # if the hand is in play, hit the player
    if in_play:
        # deal a card to player hand
        player_hand.add_card(my_deck.deal_card())

        # calculate value and print to screen
        prompt = "Hit or stand?"
        print "Player hits and is dealt a", player_hand.cards[-1], "for a hand value of", player_hand.get_value()

        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            prompt = "You busted! Dealer wins. Deal again?"
            outcome = "You busted! Dealer wins. Score ="
            in_play = False
            score -= 1
            player_busted = True
            print outcome, score
    else:
        prompt = "The round is over. Deal again?"
        print "\nThe round is over. Deal again?"



def stand():
    global player_hand, in_play, score, outcome, dealer_hand, my_deck, player_busted, prompt

    # check if player already busted
    if player_busted:
        prompt = "Too late to stand now, you already busted. Deal again?"
        print "\nIt's too late, you already busted with a hand value of", str(player_hand.get_value()) + "... \nNo shame in going for it all though! Deal again?"

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
            print "Dealer hits and is dealt a", dealer_hand.cards[-1], "for a hand value of", dealer_hand.get_value()
            if dealer_hand.get_value() > 21:
                prompt = "Dealer busted! You win. Deal again?"
                outcome = "You win! Dealer busted with a hand value of"
                score += 1
                print outcome, str(dealer_hand.get_value()) + ". Score =", score
        if 17 <= dealer_hand.get_value() <= 21:
            if player_hand.get_value() < dealer_hand.get_value():
                prompt = "You played well, but the Dealer was better. Deal again?"
                outcome = "Dealer wins! Score ="
                score -= 1
                print outcome, score
            elif player_hand.get_value() == dealer_hand.get_value():
                prompt = "It's a draw! Tie goes to the dealer. Deal again?"
                outcome = "It's a draw! Tie goes to the dealer. Score ="
                score -= 1
                print outcome, score
            else:
                prompt = "Well played, you win! Deal again?"
                outcome = "You win! Score ="
                score += 1
                print outcome, score
    elif in_play and not player_busted:
        prompt = "The round is over. Deal again?"
        print "\nThe round is over. Play again?"

    in_play = False



# draw handler
def draw(canvas):
    # use draw method in Hand class to draw player and dealer's hands

    # dealer hand
    canvas.draw_text("Dealer:", [100, 75], 18, "White", "monospace")
    if in_play:
        dealer_hand.draw(canvas, [100,100])
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        dealer_hand.draw(canvas, [100,100])

    # player hand
    canvas.draw_text("Player:", [100, 275], 18, "White", "monospace")
    player_hand.draw(canvas, [100,300])

    # score
    score_board = "Score = " + str(score)
    canvas.draw_text(score_board, [475, 25], 18, "White", "monospace")

    # gameplay prompts
    # get the width of the prompt in pixels
    text_width = frame.get_canvas_textwidth(prompt, 18, "monospace")
    # center text based on prompt width
    prompt_pos = [(CANVAS_WIDTH/2) - (text_width/2), 500 ]
    canvas.draw_text(prompt, prompt_pos, 18, "White", "monospace")



# initialization frame
frame = simplegui.create_frame("Blackjack", CANVAS_WIDTH, CANVAS_HEIGHT)
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
