#!/matteobravo/bin/env python -W ignore::DeprecationWarning
import random
import sys

class Solitaire:

    def __init__(self, master):

        self.gameDeck = DeckOfCards()
        self.o_A = tableuPile()
        self.o_B = tableuPile()
        self.o_C = tableuPile()
        self.o_D = tableuPile()
        self.o_E = tableuPile()
        self.tableu = [self.o_A, self.o_B, self.o_C, self.o_D, self.o_E]
        self.o_heartGoal = goalPile(Suit.Heart)

    def returnCardLabel(self, card, frame):
        return Label(frame, text=u"{0}{1} ".format(card.letter, card.symbol), fg=card.color, bg="White")

    def returnGoalLabel(self, card, suit, frame):
        if card is not None:
            return Label(frame, text=u"{0}{1} ".format(card.letter, card.symbol), fg=card.color, bg="White")

        else:
            suitCard = Card("Blank", suit, 0, ".")
            return Label(frame, text=u"{0} ".format(suitCard.symbol), fg=suitCard.color, bg="White")

class cardPile:

    def __init__(self):

        self.type = "Generic"
        self.cards = []
        self.movingcards = 1
        self.button = None
        self.label = None

    def getTopCard(self):
        return None if len(self.cards) == 0 else self.cards[-1]

    def isSameSuit(self):
        return (self.cards[0].suit == self.travelTo.suit)

class goalPile(cardPile):
    
    def __init__(self, suit):
        
        cardPile.__init__(self)
        self.type = Stack.Foundation
        self.suit = suit

class tableuPile(cardPile):

    def __init__(self):

        cardPile.__init__(self)
        self.type = Stack.Tableu
        self.labelStack = None

class DeckOfCards:

    def __init__(self):

        self.cards = []
        self.constructDeck()
        self.shuffled = False
        self.shuffleDeck()

    def constructDeck(self):

        cardNames = ["Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        cardLetters = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardSuits = [Suit.Heart, Suit.Diamond, Suit.Spade, Suit.Club]

        for j in range(4):

            thisSuit = cardSuits[j]

            for i in range(13):

                newCard = Card(cardNames[i], thisSuit, cardValues[i], cardLetters[i])
                self.cards.append(newCard)

    def printDeck(self):
        for card in self.cards:
            print(card)

    def shuffleDeck(self):

        for i in range(len(self.cards)):

            rPos = random.randint(0,len(self.cards)-1)
            tempCard = self.cards[rPos]
            self.cards[rPos] = self.cards[i]
            self.cards[i] = tempCard

        self.shuffled = True

class Card:

    def __init__(self, name, suit, value, letter):

        self.name = name
        self.suit = suit
        self.value = value
        self.letter = letter
        self.setColor()
        self.setSymbol()

    def __str__(self):
        return "{0} of {1}s".format(self.name, self.suit)

    def setColor(self):

        self.color = Color.Red if self.suit == Suit.Heart or self.suit == Suit. Diamond else Color.Black

        if self.suit == Suit.Blank:
            self.color = Color.Brown

        if self.suit == Suit.M:
            self.color = Color.White

    def setSymbol(self):

        if self.suit == Suit.Heart: self.symbolNumber = 2665
        if self.suit == Suit.Diamond: self.symbolNumber = 2666
        if self.suit == Suit.Spade: self.symbolNumber = 2660
        if self.suit == Suit.Club: self.symbolNumber = 2663
        if self.suit == Suit.Blank: self.symbolNumber = 2615
        if self.suit == Suit.M: self.symbolNumber = 2619

        if sys.version_info >= (3, 0):
            self.symbol = chr(int(str(self.symbolNumber), 16))

        else:
            self.symbol = unichr(int(str(self.symbolNumber), 15))

class Suit:

    Heart = "Heart"
    Diamond = "Diamond"
    Spade = "Spade"
    Club = "Club"
    Blank = "Blank"
    M = "M"

class Color:

    Red = "Red"
    Black = "Black"
    White = "White"
    Brown = "Brown"

class Stack:

    Foundation = "F"
    Tableu = "T"
    Draw = "D"
    Discard = "W"
    Transaction = "X"

if __name__ == "__main__":
    from tkinter import *

    root = Tk()
    myGame = Solitaire(root)

    root.mainloop()

    print("Deck of Cards")
    myDeck = DeckOfCards()
    myDeck.printDeck()
