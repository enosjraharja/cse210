import random
import os
 
# Function to clear the terminal
def clear():
    os.system("clear")
 
# Function to print the scorebaord  
def print_scoreboard(score, chances):
    print("\t\t\t     ____________________")
    print("\t\t\t    |                    |")
    if score >= 10:
        print("\t\t\t    |     Score = {}     |".format(score))
    else:   
        print("\t\t\t    |     Score = {}      |".format(score))
    print("\t\t\t    |  Chances Left = {}  |".format(chances))  
    print("\t\t\t    |____________________|")
 
# Function to print the cards
def print_cards(prev_card, current_card):
     
    print()
    print("\t ________________      ________________      ________________")
    print("\t|                |    |                |    |                |")
    if prev_card.value == '10' and current_card.value == '10':
        print("\t|  {}            |    |  {}            |    |                |".format(prev_card.value,current_card.value))
    elif prev_card.value == '10': 
        print("\t|  {}            |    |  {}             |    |                |".format(prev_card.value,current_card.value))   
    elif current_card.value == '10':
        print("\t|  {}             |    |  {}            |    |                |".format(prev_card.value,current_card.value))   
    else:
        print("\t|  {}             |    |  {}             |    |                |".format(prev_card.value,current_card.value))  
    print("\t|                |    |                |    |      * *       |")
    print("\t|                |    |                |    |    *     *     |")
    print("\t|                |    |                |    |   *       *    |")
    print("\t|                |    |                |    |   *       *    |")
    print("\t|       {}        |    |       {}        |    |          *     |".format(prev_card.suit, current_card.suit))
    print("\t|                |    |                |    |         *      |")
    print("\t|                |    |                |    |        *       |")
    print("\t|                |    |                |    |                |")
    print("\t|                |    |                |    |                |")
    if prev_card.value == '10' and current_card.value == '10':
        print("\t|            {}  |    |            {}  |    |        *       |".format(prev_card.value,current_card.value))
    elif prev_card.value == '10': 
        print("\t|            {}  |    |            {}   |    |        *       |".format(prev_card.value,current_card.value))   
    elif current_card.value == '10':
        print("\t|            {}   |    |            {}  |    |        *       |".format(prev_card.value,current_card.value))   
    else:
        print("\t|            {}   |    |            {}   |    |        *       |".format(prev_card.value,current_card.value))  
    print("\t|________________|    |________________|    |________________|")
    print()
 
 
# The Card class definition
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
 
def hi_lo_game(deck):
 
    global cards_values
 
    # Initialize the previous card
    prev_card = Card(" ", " ")
 
    # Initialize the current card
    current_card = random.choice(deck)
 
    # The starting card cannot be lowest or highest
    while current_card.value == "A" or current_card.value == "K":
        current_card = random.choice(deck)
 
    # Remove the card from the deck 
    deck.remove(current_card)
 
    # Number of chances left
    chances = 3
 
    # The current
    score = 0
 
    # The GAME LOOP
    while chances:
 
        print_scoreboard(score, chances)
        print_cards(prev_card, current_card)
 
        print("\t\t   ------------------------------------")
        print("\t\t\t\tGAME MENU")
        print("\t\t   ------------------------------------")
        print()
        print("\t\t      Enter 1 to bet for a high card")
        print("\t\t      Enter 0 to bet for a low card")
        print()
         
        # Check if we reached the end of the deck
        if len(deck) == 0:
            clear()
            print_cards(prev_card, current_card)
            print("\t\t    YOU HAVE REACHED THE END OF THE DECK!")
            print("\t\t           Congratulations!!!")
            print()
            print("\t\t          Your Final Score =", score)
            print("\t\t        Thank you for playing!!!")
            break
 
        # Try block for player input error
        try:
            choice = int(input("\t\t\t  Enter your choice = "))
        except ValueError:
            clear()
            print("\t\t\tWrong Input!! Try Again.")
            continue   
 
        # Some wrong choice
        if choice > 1 or choice < 0:
            clear()
            print("\t\t\tWrong Input!! Try Again.")
            continue       
 
        # Switch the current card to the previous card
        prev_card = current_card
 
        # Choose the new current card
        current_card = random.choice(deck)
 
        # Remove the new card from the deck
        deck.remove(current_card)
 
        # A high card
        if cards_values[current_card.value] > cards_values[prev_card.value]:
            result = 1
 
        # A low card    
        elif cards_values[current_card.value] < cards_values[prev_card.value]:
            result = 0
 
        # Same value card   
        else:
            result = -1    
 
        # A Tie Round
        if result == -1:
            clear()
            print("\t\t\t TIE GAME!! Play Again")
 
        # Round won
        elif choice == result:
            clear()
            print("\t\t\t YOU WIN!!! Play Again")
            score = score + 1  
 
        # Round Lost    
        else:
            if chances == 1:
                clear()
                print("\t\t\t\tGAME OVER")
                print_cards(prev_card, current_card)
                print("\t\t        Your Final Score =", score)
                print("\t\t      Thank you for playing!!!")
                break  
            clear()
            print("\t\t\t YOU LOSE!! Play Again")
            chances = chances - 1
 
 
if __name__ == '__main__':
 
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
    # The suit value 
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # The card value
    cards_values = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
 
    # The deck of cards
    deck = []
 
    # Loop for every type of suit
    for suit in suits:
 
        # Loop for every type of card in a suit
        for card in cards:
 
            # Adding card to the deck
            deck.append(Card(suits_values[suit], card))
 
    hi_lo_game(deck)
