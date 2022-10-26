import random

class Deck:

    def __init__(self):
        self.cards = []
        
    def addCard(self, card):
        self.cards.append(card)

    def getDeck(self):
        return self.cards

    def dealCard(self):
        c = random.choice(self.cards)
        self.cards.remove(c)
        return c

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def getSuit(self):
        return self.suit

    def getName(self):
        return self.name

    def getCard(self):
        return self.suit, self.name

def main():

    D = Deck()

    suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    for s in suits:
        for i in range(1, 14):
            if i == 1:
                name = "Ace"
            elif i == 11:
                name = "Jack"
            elif i == 12:
                name = "Queen"
            elif i == 13:
                name = "King"
            else:
                name = str(i)
            C = Card(s, name)
            D.addCard(C)

    card1 = D.dealCard()
    card2 = D.dealCard()
    card3 = D.dealCard()
    card4 = D.dealCard()

    userHand = [card1.getCard(), card2.getCard()]
    dealerHand = [card3.getCard(), card4.getCard()]

    print("Welcome to Blackjack!")
    print("Here is your hand:")
    print(userHand)
    print("Here is the dealer's hand:")
    print(dealerHand)
    

    

if __name__ == "__main__":
    main()
