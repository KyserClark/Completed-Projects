#!/usr/bin/env python3

"""
Kyser Clark's Blackjack
@KyserClark
KyserClark.com

Thank you for reading my code!
This is my 2nd completed project in any programming language
It took me 23 hours to go from a blank slate to this
I'm still pretty new to programming
(only 82 Hours of learning and practice at this point)
So it might not be the cleanest code,
but this is the best my abilities can come up with for now.
Feel free to contact me and give me constructive criticism
I'm interested in learning and getting better,
so don't hold back when giving feedback

"""

# Global variables
import random

# Card attributes for card class
suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}


# Aces are high (11) until they need to be low (1)


class Card:
    # Class that creates a single card and stores card attributes
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        # Method that prints out a single card
        return f"{self.rank} of {self.suit}"


class Deck:
    # Class that creates a new 52 card deck and stores card attributes
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))

    def shuffle(self):
        # Method that shuffles a deck
        random.shuffle(self.all_cards)

    def deal(self):
        # Method that removes top card of the deck
        return self.all_cards.pop(0)


class Hand:
    # Class that tracks what cards are in hand, total value of the cards 
    # and determines if aces are high or low for the hand
    def __init__(self):
        self.cards = []  # start with zero cards
        self.value = 0  # start with zero value
        self.aces = 0  # attribute to keep track of aces

    def add_card(self, dealt_card):
        # Method that deals top card from the deck to the hand 
        # and takes record of Aces in hand
        # Subtracts 10 from total value for each Ace over 21
        self.cards.append(dealt_card)
        if dealt_card.rank == 'Ace':
            self.aces += 1
        self.value += dealt_card.value
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def show_hand(self):
        # Method that prints out every card in the current hand
        for card_object in self.cards:
            print(card_object)


class Chips:
    # Class that stores total chip balance and current bet amount
    def __init__(self, total, bet):
        self.total = total
        self.bet = bet

    def win_bet(self):
        # Method that adds bet amount to player chip balance
        self.total += self.bet

    def lose_bet(self):
        # Method that removes bet amount from player chip balance
        self.total -= self.bet

    def __str__(self):
        # Method to print current chip balance
        return f"\nChip Balance is {self.total}\n"


def take_bet():
    # Function that asks player to input a bet 
    # and stores bet amount in Chip class.
    while True:
        try:
            print(f"\nYour Chip Balance is: {balance.total}\n")
            print("\nBet must be between 2 and 500")
            balance.bet = int(input("\nPLACE YOUR BET: \n"))

        # while loop continues if user input is not an integer    
        except ValueError:
            print("\nError: Input an integer\n")
            continue

        else:
            # Valid Bet, break out of while loop
            if balance.bet <= balance.total and 1 < balance.bet < 501:
                print(f"\nGood luck!!\n")
                break

            # Invalid Bet, continue while loop    
            if balance.bet > balance.total:
                print("\nCan't place bet because it exceeds your chip "
                      "balance\n")
                continue


def hit(hand):
    # Function that adds top card of the deck to hand
    hand.add_card(new_deck.deal())


def hit_or_stand():
    # Function that asks players if they want to Hit or Stand
    global choice  # choice is used later to determine flow of game-play

    while True:  # Loop until choice is valid
        choice = input("(H)IT or (S)TAND? : ").upper()
        if choice in ["HIT", "STAND", "H", "S"]:
            break
        else:
            print("\nChoice not valid, try again\n")

    if choice in ["HIT", "H"]:  # If player hits, run hit function
        hit(player_hand)


def show_some(player, dealer):
    # Function that reveals 1st dealer card 
    # and emulates the 2nd card being face down
    # Then shows player full hand
    print("\n----------------")
    print("\n[DEALER's HAND]\n")
    print(dealer.cards[0])
    print("HIDDEN CARD\n")
    print("----------------")
    print("\n[PLAYER's HAND]\n")
    for card_object in player.cards:
        print(card_object)
    print("\n----------------\n")


def show_all(player, dealer):
    # Function that shows all player and all dealer cards
    print("\n----------------")
    print("[PLAYER's HAND]\n")
    for card_object in player.cards:
        print(card_object)
    print("\n----------------")
    print("\n[DEALER's HAND]\n")
    for card_object in dealer.cards:
        print(card_object)
    print("\n----------------\n")


def player_busts():
    print("\nYOU BUST\n")
    dealer_wins()


def player_wins():
    balance.win_bet()
    print(f"\nYOU WIN!!\nYou earned {balance.bet} Chips!\n")


def dealer_busts():
    print("\nDEALER BUSTS\n")
    player_wins()


def dealer_wins():
    balance.lose_bet()
    print(f"\nDEALER WINS\nYou lost {balance.bet} Chips\n")


def push():
    print("\nIt's a PUSH (tie)\n\nBet returned to your Chip Balance\n")


def play_again():
    # Play choice used later to determine if player wants to play again.
    global play_choice
    while True:
        play_choice = \
            input("\nWould you like to play again? Y or N:\n").upper()
        if play_choice not in ["YES", "NO", "Y", "N"]:
            print("\nChoice not valid, try again\n")
        else:
            break


# Start the Game
print("Welcome to Kyser Clark's Blackjack!!\n")
print("Thank you for checking it out!")
print("This is a one player game where you play against the Dealer.")
print("The goal of the game is to get your hand closer to 21 "
      "than the Dealer's hand.")

print("A hand value greater than 21 is called a BUST "
      "(Hand is a losing hand).")

print("The Dealer will always HIT if their hand is below 17.")
print("The Dealer will always STAND if their hand is 17 or greater.")
print("Your starting chip balance is 100. Minimum bet is 2 chips, "
      "Maximum bet is 500 chips")

print("If you have a Blackjack, your payout is 3 to 2 (150%)")
print("For the sake of simplicity, you cannot double-down, "
      "place insurance, or split.")

print("You can only (H)IT, or (S)TAND.")
print("You lose the game if your chip balance is below 1, "
      "but don't worry, you can always play again.")

print("Number Cards are worth their number value.")
print("Face Cards (Jack, Queen, and King) are worth 10.")
print("Aces are worth 1 or 11. "
      "Whichever is more beneficial to the hand.")

print("The 52 card deck is shuffled after 5 hands have been dealt. "
      "This is to YOUR advantage")

print("For feedback, you can reach me @KyserClark or KyserClark.com\n")
input("Press ENTER to start playing")

# Create player balance using Chip Class
# Set Player Chip Balance to 100, 
# and Bet amount to 0 when starting new game
balance = Chips(100, 0)
# Create and shuffle a new deck to start game
new_deck = Deck()
new_deck.shuffle()
hands_played = 0  # Keeps track of hands played, start at 0

while True:
    if hands_played >= 5:  # Only if 5 hands have been played
        # Create & shuffle a new deck
        new_deck = Deck()
        new_deck.shuffle()
        # Inform player that the deck has been shuffled
        print("\nTHE DECK HAS BEEN SHUFFLED\n")
        hands_played = 0  # Reset hands played count

    # Informs player the amount of hands played since last shuffle
    print(f"Hands played since last shuffle: {hands_played}")

    # Creates / resets hands using Hand Class
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal two cards to each player
    player_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())

    # Prompt the Player for their bet
    take_bet()

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    # Check for natural Blackjacks
    if player_hand.value == 21:
        print("YOU HAVE A BLACKJACK!!!")
        player_blackjack = True
        # Change bet amount so Player gets paid 3:2 (150%) of their bet
        balance.bet = int(balance.bet * 1.5)
    else:
        player_blackjack = False

    if dealer_hand.value == 21:
        print("Dealer has a Blackjack!!!")
        dealer_blackjack = True
    else:
        dealer_blackjack = False

    # Only play if neither player or dealer has Blackjack
    if not dealer_blackjack and not player_blackjack:
        while True:

            # Prompt for Player to Hit or Stand
            hit_or_stand()

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, 
            # run player_busts() and break out of loop
            if player_hand.value > 21:
                show_all(player_hand, dealer_hand)  # Show all cards
                player_busts()
                break

            # If player stands, break out of loop
            if choice in ["STAND", "S"]:
                break

    # Only play dealer hand if neither player or dealer has Blackjack 
    # and if player didn't bust
    if player_hand.value <= 21 and not player_blackjack and not \
            dealer_blackjack:
        # Show all cards to reveal dealer hidden card to player
        show_all(player_hand, dealer_hand)

        # Dealer must hit until they reach 17 or more
        while dealer_hand.value < 17:
            input("\nDealer must HIT, Press Enter to see next card: \n")
            # Add card to dealer hand
            dealer_hand.add_card(new_deck.deal())
            # Show all cards to show the new dealer card
            show_all(player_hand, dealer_hand)

            # Show All Cards (only if player didn't bust)
    if player_hand.value <= 21:
        show_all(player_hand, dealer_hand)

    # Check for win conditions
    # run win functions only if player didn't bust    
    if dealer_hand.value > 21 >= player_hand.value:
        dealer_busts()

    if player_hand.value < dealer_hand.value <= 21 and \
            player_hand.value <= 21:
        dealer_wins()

    if dealer_hand.value < player_hand.value <= 21 and \
            player_hand.value <= 21:
        player_wins()

    if player_hand.value == dealer_hand.value and player_hand.value <= 21:
        push()

    # Inform player of their chips total
    print(f"\nYour Chip Balance is: {balance.total}\n")

    # Add 1 to the hands played tally
    hands_played += 1

    # Check Chip Balance for GAME OVER Condition    
    if balance.total > 1:
        play_again()

    if balance.total <= 1:
        print("GAME OVER You are out of Chips")
        play_again()
        if play_choice in ["YES", "Y"]:
            # Reset Player Chip Balance to 100
            # Reset Bet amount to 0 if player wants to play again
            balance = Chips(100, 0)

    # Break loop and close program if player doesn't want to play again
    if play_choice in ["NO", "N"]:
        break
